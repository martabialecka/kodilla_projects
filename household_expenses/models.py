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
        expenses = [expense for expense in self.all() if expense['id'] == id]
        if expenses:
            return expenses[0]
        return []

    def create(self, data):
        self.data.append(data)
        self.save_all()

    def save_all(self):
        with open("hh_expenses.json", "w") as f:
            json.dump(self.data, f)

    def update(self, id, data):
        expense = self.get(id)
        if expense:
            index = self.data.index(expense)
            self.data[index] = data
            self.save_all()
            return True
        return False

    def delete(self, id):
        expense = self.get(id)
        if expense:
            self.data.remove(expense)
            self.save_all()
            return True
        return False

hh_expenses = HHExpenses()
