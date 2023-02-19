from flask import Flask, request, render_template, redirect, url_for
from forms import ExpensesForm
from models import hh_expenses

app = Flask(__name__)
app.config["SECRET_KEY"] = "lalala"

@app.route("/expenses/", methods=["GET", "POST"])
def hh_expenses_list():
    form = ExpensesForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            hh_expenses.create(form.data)
            hh_expenses.save_all()
        return redirect(url_for("hh_expenses_list"))

    return render_template(                     \
        "hh_expenses.html",                     \
        form = form,                            \
        hh_expenses = hh_expenses.all(),        \
        unpaid_sum = hh_expenses.unpaid_sum(),  \
        error = error)

@app.route("/expenses/<int:expense_id>/", methods=["GET", "POST"])
def hh_expense_details(expense_id):
    expenses = hh_expenses.get(expense_id - 1)
    form = ExpensesForm(data = expenses)

    if request.method == "POST":
        if form.validate_on_submit():
            hh_expenses.update(expense_id - 1, form.data)
        return redirect(url_for("hh_expenses_list"))
    return render_template("hh_expense.html", form = form, expense_id = expense_id)


if __name__ == "__main__":
    app.run(debug=True)
