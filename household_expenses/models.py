import json

def prepare_new_record(new_record, id):
    new_record.pop('csrf_token', None)
    new_record['id'] = id
    new_record['amount'] = float(new_record['amount'])
    return new_record

class HHExpenses:
    def __init__(self):
        try:
            with open('hh_expenses.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = []

    def new_id(self):
        if self.data:
            return self.data[-1]['id'] + 1
        return 0

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
        new_record = prepare_new_record(new_record, self.new_id())
        self.data.append(new_record)
        self.save_all()

    def update(self, id, new_record):
        old_record = self.get(id)
        if old_record:
            index = self.data.index(old_record)
            new_record = prepare_new_record(new_record, id)
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
    
    def unpaid_sum (self):
        result = 0
        for item in self.data:
            if not item['paid']:
                result += item['amount']
        return result

hh_expenses = HHExpenses()
