To run the "Household expenses", install python 3.x and execute
pip install -r requirements.txt
Next, go to the folder with app.py file and launch "flask --app app.py run" command.

The app exposes REST api at address http://localhost:5000/api/expenses
The API supports GET, POST, PUT and DELETE requestes.
For PUT, DELETE use an address in the form http://localhost:5000/api/expenses/<int:expense_id>
Optionally such an address can be used with GET to get details of a single expense.

The app can be used with a web browser at address http://localhost:5000/expenses
