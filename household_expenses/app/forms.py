from flask_wtf import FlaskForm
from wtforms import BooleanField, DecimalField, StringField
from wtforms.validators import DataRequired

class ExpensesForm(FlaskForm):
    name = StringField('Nazwa', validators=[DataRequired()])
    amount = DecimalField('Kwota', validators=[DataRequired()])
    paid = BooleanField ('Zapłacone?')

    def get_float_string(self, f):
        return ('%.2f' % f).replace('.', ',')
