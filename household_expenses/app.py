from flask import Flask, jsonify
from models import hh_expenses

from flask import abort

from flask import make_response

from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lalala'


@app.route('/api/v1/expenses/', methods=['GET'])
def expenses_list_api_v1():
    return jsonify(hh_expenses.all())

@app.route('/api/v1/expenses/<int:expense_id>', methods=['GET'])
def get_expenses(expense_id):
    expenses = hh_expenses.get(expense_id)
    if not expenses:
        abort(404)
    return jsonify({'expenses': expenses})

@app.route('/api/v1/expenses/', methods=['POST'])
def create_expenses():
    if not request.json:
        abort(400)
    
    data = request.json

    if not 'title' in data:
        abort(400)
    if not isinstance(data['title'], str):
        abort(400)
    if 'amount' in data and not isinstance(data['amount'], float) and not isinstance(data['amount'], int):
        abort(400)
    if 'paid' in data and not isinstance(data['paid'], bool):
        abort(400)

    expense = {
        'id': hh_expenses.all()[-1]['id'] + 1 if hh_expenses.all() else 0,
        'title': data['title'],
        'amount': float(data.get('amount', 0.0)),
        'paid': data.get('paid', False)
    }
    hh_expenses.create(expense)
    return jsonify({'expenses': expense}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

@app.route('/api/v1/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expenses(expense_id):
    result = hh_expenses.delete(expense_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.route('/api/v1/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    expense = hh_expenses.get(expense_id)

    if not expense:
        abort(404)
    if not request.json:
        abort(400)
    
    data = request.json
    
    if 'title' in data and not isinstance(data['title'], str):
        abort(400)
    if 'amount' in data and not isinstance(data['amount'], float) and not isinstance(data['amount'], int):
        abort(400)
    if 'paid' in data and not isinstance(data['paid'], bool):
        abort(400)

    expense = {
        'id': expense_id,
        'title': data.get('title', expense['title']),
        'amount': float(data.get('amount', expense['amount'])),
        'paid': data.get('paid', expense['paid'])
    }
    hh_expenses.update(expense_id, expense)
    return jsonify({'expenses': expense})