from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField


class LoginForm(FlaskForm):
    employee_number = StringField('Employee Number')
    password = PasswordField('Password')
    submit = SubmitField('Submit')


class AssignEmployeeForm(FlaskForm):
    employee_name = SelectField('Employee Name')
    tables = SelectField('Table Number')
    submit = SubmitField('Submit')


class CloseTable(FlaskForm):
    tables = SelectField('Table Number')
    submit = SubmitField('Close Table')


class AddFood(FlaskForm):
    menu_items = SelectField('Menu Items')
    order = SelectField('Order')
