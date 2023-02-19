import json


class HHExpenses:
    def __init__(self):
        try:
            with open("hh_expenses.json", "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = []

    def all(self):
        return self.data

    def get(self, id):
        return self.data[id]

    def create(self, data):
        data.pop('csrf_token')
        self.data.append(data)

    def save_all(self):
        with open("hh_expenses.json", "w") as f:
            json.dump(self.data, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.data[id] = data
        self.save_all()
    
    def unpaid_sum (self):
        result = 0
        for expense in self.data:
            if not expense['paid']:
                result += expense['amount']
        return result

hh_expenses = HHExpenses()
