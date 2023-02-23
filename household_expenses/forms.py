from flask_wtf import FlaskForm
from wtforms import BooleanField, FloatField, StringField
from wtforms.validators import DataRequired

class ExpensesForm(FlaskForm):
    title = StringField('Nazwa', validators=[DataRequired()])
    amount = FloatField('Kwota', validators=[DataRequired()])
    paid = BooleanField ('Zapłacone?')
