To run the "Household expenses", install python 3.x and execute
pip install -r requirements.txt

From household_expenses directory execute

flask db init
flask db migrate
flask db upgrade
flask run

The app stores data in household_expenses.db SQLite database.
The app exposes REST api at address http://localhost:5000/api/expenses
The API supports GET, POST, PUT and DELETE requestes.
For PUT, DELETE use an address in the form http://localhost:5000/api/expenses/<int:expense_id>
Optionally such an address can be used with GET to get details of a single expense.

The app can be used with a web browser at address http://localhost:5000/expenses
