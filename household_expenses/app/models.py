import json
from app import db, app
from sqlalchemy import Integer
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import cast, not_

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, index = True)
    amount = db.Column(db.Float)
    paid = db.Column(db.Boolean)

    def __init__(self, new_record):
        self.from_dict(new_record)
    
    def from_dict(self, d):
        for key in d:
            if key != 'id':
                setattr(self, key, d[key])

    def to_dict(self):
        return {k: v for k, v in vars(self).items() if not k.startswith('_')}

def prepare_new_record(new_record):
    new_record.pop('csrf_token', None)
    new_record['amount'] = float(new_record['amount'])
    return new_record

class HHExpenses:
    def __init__(self):
        with app.app_context():
            # not paid sum = sum(amount * not paid)
            self.query_sum = db.session.query(func.sum(Expense.amount * cast(not_(Expense.paid), Integer)))

    def all(self):
        return [e.to_dict() for e in Expense.query.all()]

    def get(self, id):
        e = Expense.query.get(id)
        if e is not None:
            return e.to_dict()
        return []

    def create(self, new_record):
        new_record = prepare_new_record(new_record)
        e = Expense(new_record)
        db.session.add(e)
        db.session.commit()

    def update(self, id, new_record):
        record = Expense.query.get(id)
        if record is not None:
            new_record = prepare_new_record(new_record)
            record.from_dict(new_record)
            db.session.add(record)
            db.session.commit()
            return True
        return False

    def delete(self, id):
        return False
    """
        record = self.get(id)
        if record:
            self.data.remove(record)
            self.save_all()
            return True
        return False
    """

    def unpaid_sum (self):
        return self.query_sum.all()[0][0]

hh_expenses = HHExpenses()
