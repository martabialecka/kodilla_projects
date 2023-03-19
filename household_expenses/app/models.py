import json
from app import db

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, index = True)
    amount = db.Column(db.Float)
    paid = db.Column(db.Boolean)

    def __init__(self, new_record):
        for key in new_record:
            if key != 'id':
                setattr(self, key, new_record[key])
    
    def to_dict(self):
        return {k: v for k, v in vars(self).items() if not k.startswith('_')}

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
        return [e.to_dict() for e in Expense.query.all()]

    def get(self, id):
        for record in self.data:
            if record['id'] == id:
                return record
        return []

    def create(self, new_record):
        new_record = prepare_new_record(new_record, self.new_id())
        self.data.append(new_record)
        self.save_all()
        ###
        e = Expense(new_record)
        db.session.add(e)
        db.session.commit()

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
