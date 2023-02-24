from flask_wtf import FlaskForm
from wtforms import BooleanField, DecimalField, StringField
from wtforms.validators import DataRequired

class ExpensesForm(FlaskForm):
    title = StringField('Nazwa', validators=[DataRequired()])
    amount = DecimalField('Kwota', validators=[DataRequired()])
    paid = BooleanField ('Zapłacone?')
