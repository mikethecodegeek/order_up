from flask import Blueprint, redirect, render_template, url_for
# from flask_login import current_user, login_user, logout_user
from app.forms import AssignEmployeeForm, CloseTable, AddFood
from app.models import (Employee, Menu, MenuItemType,
                        MenuItem, Order, OrderDetail, Table)


bp = Blueprint("forms", __name__, url_prefix='/manage')


@bp.route("/", methods=["GET", "POST"])
def assign_employee():
    form = AssignEmployeeForm()
    employee = Employee.query.all()
    employees = [(e.id, f"Employee {e.name}") for e in employee]
    if form.validate_on_submit():
        pass
    return render_template('assign.html', form=form, employees=employees)
