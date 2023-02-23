import json

class HHExpenses:
    def __init__(self):
        try:
            with open('hh_expenses.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = []

    def save_all(self):
        with open('hh_expenses.json', 'w') as f:
            json.dump(self.data, f)

    def all(self):
        return self.data

    def get(self, id):
        for record in self.data:
            if record['id'] == id:
                return record
        return []

    def create(self, new_record):
        self.data.append(new_record)
        self.save_all()

    def update(self, id, new_record):
        old_record = self.get(id)
        if old_record:
            index = self.data.index(old_record)
            self.data[index] = new_record
            self.save_all()
            return True
        return False

    def delete(self, id):
        record = self.get(id)
        if record:
            self.data.remove(record)
            self.save_all()
            return True
        return False

hh_expenses = HHExpenses()
