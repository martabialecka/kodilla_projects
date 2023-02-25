from flask import Flask
from flask import abort, jsonify, make_response, redirect, render_template, url_for
from flask import request
from models import hh_expenses
from forms import ExpensesForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lalala'

@app.route('/api/expenses/', methods=['GET'])
def get_expenses():
    return jsonify({'expenses': hh_expenses.all(), 'unpaid' : hh_expenses.unpaid_sum()})

@app.route('/api/expenses/<int:expense_id>', methods=['GET'])
def get_expense(expense_id):
    expenses = hh_expenses.get(expense_id)
    if not expenses:
        abort(404)
    return jsonify({'expense': expenses})

@app.route('/api/expenses/', methods=['POST'])
def create_expense():
    if not request.json:
        abort(400)
    
    data = request.json

    if not 'name' in data:
        abort(400)
    if not isinstance(data['name'], str):
        abort(400)
    if 'amount' in data and not isinstance(data['amount'], float) and not isinstance(data['amount'], int):
        abort(400)
    if 'paid' in data and not isinstance(data['paid'], bool):
        abort(400)

    expense = {
        'name': data['name'],
        'amount': float(data.get('amount', 0.0)),
        'paid': data.get('paid', False)
    }
    hh_expenses.create(expense)
    return jsonify({'expense': expense}), 201

@app.route('/api/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    expense = hh_expenses.get(expense_id)

    if not expense:
        abort(404)
    if not request.json:
        abort(400)
    
    data = request.json
    
    if 'name' in data and not isinstance(data['name'], str):
        abort(400)
    if 'amount' in data and not isinstance(data['amount'], float) and not isinstance(data['amount'], int):
        abort(400)
    if 'paid' in data and not isinstance(data['paid'], bool):
        abort(400)

    expense = {
        'name': data.get('name', expense['name']),
        'amount': float(data.get('amount', expense['amount'])),
        'paid': data.get('paid', expense['paid'])
    }
    hh_expenses.update(expense_id, expense)
    return jsonify({'expense': expense})

@app.route('/api/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    result = hh_expenses.delete(expense_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

@app.route('/expenses/', methods=['GET', 'POST'])
def main_page():
    form = ExpensesForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            hh_expenses.create(form.data)
        return redirect(url_for('main_page'))

    return render_template(                     \
        'hh_expenses.html',                     \
        form = form,                            \
        hh_expenses = hh_expenses.all(),        \
        unpaid_sum = hh_expenses.unpaid_sum())

@app.route('/expenses/<int:expense_id>/', methods=['GET', 'POST'])
def details_page(expense_id):
    expenses = hh_expenses.get(expense_id)
    form = ExpensesForm(data = expenses)

    if request.method == 'POST':
        if 'save' in request.form and form.validate_on_submit:
            hh_expenses.update(expense_id, form.data)
        elif 'delete' in request.form:
            hh_expenses.delete(expense_id)
        return redirect(url_for('main_page'))
    return render_template('hh_expense.html', form = form, expense_id = expense_id)
