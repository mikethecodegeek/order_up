from dotenv import load_dotenv
load_dotenv()
from app.models import Employee, Menu, MenuItemType, MenuItem, Table, Order, OrderDetail  # noqa
from app import app, db  # noqa


# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234,
                        password="password")
    db.session.add(employee)

    beverages = MenuItemType(name="Beverages")
    db.session.add(beverages)

    entrees = MenuItemType(name="Entrees")
    db.session.add(entrees)

    sides = MenuItemType(name="Sides")
    db.session.add(sides)

    dinner = Menu(name="Dinner")
    db.session.add(dinner)

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    db.session.add(fries)

    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    db.session.add(drp)

    jambalaya = MenuItem(name="Jambalaya", price=21.98,
                         type=entrees, menu=dinner)
    db.session.add(jambalaya)

    for x in range(1, 11):
        table = Table(number=x, capacity=4)
        db.session.add(table)

    order1 = Order(employee_id=1, table_id=1, finished=False)
    db.session.add(order1)

    order1_details = OrderDetail(order_id=1, menu_item_id=1)
    db.session.add(order1_details)
    db.session.commit()
