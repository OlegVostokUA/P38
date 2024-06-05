# # lect_29_ORM systems
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, \
#     String, DateTime, ForeignKey, Numeric, PrimaryKeyConstraint, \
#     UniqueConstraint, ForeignKeyConstraint, SmallInteger, not_, and_
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime
#
# from sqlalchemy.orm import relationship, Session
#
# engine = create_engine('sqlite:///sqlite_database.db')
# session = Session(bind=engine)
# Base = declarative_base()
#
#
# class Customer(Base):
#     __tablename__ = 'customers'
#     id = Column(Integer(), primary_key=True)
#     first_name = Column(String(100), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     username = Column(String(50), nullable=False)
#     email = Column(String(200), nullable=False)
#     created_on = Column(DateTime(), default=datetime.now)
#     updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
#     orders = relationship("Order", backref='customer')
#
#
# class Item(Base):
#     __tablename__ = 'items'
#     id = Column(Integer(), primary_key=True)
#     name = Column(String(200), nullable=False)
#     cost_price = Column(Numeric(10, 2), nullable=False)
#     selling_price = Column(Numeric(10, 2), nullable=False)
#     quantity = Column(Integer())
#
#
# class Order(Base):
#     __tablename__ = 'orders'
#     id = Column(Integer(), primary_key=True)
#     customer_id = Column(Integer(), ForeignKey('customers.id'))
#     date_placed = Column(DateTime(), default=datetime.now)
#     line_items = relationship("OrderLine", backref='order')
#
#
# class OrderLine(Base):
#     __tablename__ = 'order_lines'
#     id = Column(Integer(), primary_key=True)
#     order_id = Column(Integer, ForeignKey('orders.id'))
#     item_id = Column(Integer, ForeignKey('items.id'))
#     quantity = Column(SmallInteger())
#     item = relationship("Item")
#
#
# Base.metadata.create_all(engine)
#
# c1 = Customer(
#     first_name = 'Dmitriy',
#     last_name = 'Yatsenko',
#     username = 'Moseend',
#     email = 'moseend@mail.com'
# )
#
# c2 = Customer(
#     first_name = 'Valeriy',
#     last_name = 'Golyshkin',
#     username = 'Moseend',
#     email = 'fortioneaks@gmail.com'
# )
#
#
# c3 = Customer(
#     first_name = "Vadim",
#     last_name = "Moiseenko",
#     username = 'Moseend',
#     email = "antence73@mail.com",
# )
#
# c4 = Customer(
#     first_name = "Vladimir",
#     last_name = "Belousov",
#     username = 'Moseend',
#     email = "andescols@mail.com",
# )
#
# c5 = Customer(
#     first_name = "Tatyana",
#     last_name = "Khakimova",
#     username = 'Moseend',
#     email = "caltin1962@mail.com",
# )
#
# c6 = Customer(
#     first_name = "Pavel",
#     last_name = "Arnautov",
#     username = 'Moseend',
#     email = "lablen@mail.com",
# )
#
# # session.add(c1)
# # session.add_all([c1, c2, c3, c4, c5, c6])
# # session.commit()
# i1 = Item(name = 'Chair', cost_price = 9.21, selling_price = 10.81, quantity = 5)
# i2 = Item(name = 'Pen', cost_price = 3.45, selling_price = 4.51, quantity = 3)
# i3 = Item(name = 'Headphone', cost_price = 15.52, selling_price = 16.81, quantity = 50)
# i4 = Item(name = 'Travel Bag', cost_price = 20.1, selling_price = 24.21, quantity = 50)
# i5 = Item(name = 'Keyboard', cost_price = 20.1, selling_price = 22.11, quantity = 50)
# i6 = Item(name = 'Monitor', cost_price = 200.14, selling_price = 212.89, quantity = 50)
# i7 = Item(name = 'Watch', cost_price = 100.58, selling_price = 104.41, quantity = 50)
# i8 = Item(name = 'Water Bottle', cost_price = 20.89, selling_price = 25, quantity = 50)
#
# # session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
# # session.commit()
#
#
# o1 = Order(customer = c1)
# o2 = Order(customer = c1)
#
# line_item1 = OrderLine(order = o1, item = i1, quantity =  3)
# line_item2 = OrderLine(order = o1, item = i2, quantity =  2)
# line_item3 = OrderLine(order = o2, item = i1, quantity =  1)
# line_item4 = OrderLine(order = o2, item = i2, quantity =  4)
#
# # session.add_all([o1, o2])
# # session.commit()
# ####################
# #print(session.query(Customer.first_name).filter(Customer.last_name == 'Arnautov').all())
#
# # print(session.query(Item.name).filter(not_(Item.cost_price.between(10, 50))).all())
# # print(session.query(Item.name).filter(Item.cost_price.between(10, 50)).all())
#
# # print(session.query(Item.name, Item.quantity).all())
# # print()
# # session.query(Item).filter(Item.name.ilike('W%')).update({'quantity': 550})
# # # session.commit()
# # # it = session.query(Item).get(3)
# # # # print(it.name)
# # # it.selling_price = 9999.99
# # # session.add(it)
# # # session.commit()
# # print(session.query(Item.name, Item.quantity).all())
# ### delete
#
# # print(session.query(Item.name, Item.quantity).all())
# # print()
# # session.query(Item).filter(Item.name.ilike('W%')).delete()
# # session.commit()
# #
# # print(session.query(Item.name, Item.quantity).all())
#
# from sqlalchemy import text
#
# print(session.query(Customer.last_name).filter(text("first_name == 'Vadim'")).all())
#
# print(session.query(Customer.last_name).filter(text("first_name LIKE 'V%'")).all())
#
# print(session.query(Customer.last_name).filter(text("first_name LIKE 'V%'")).order_by(text('last_name DESC')).all())

from pony import orm

db = orm.Database()

class User(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str)
    age = orm.Required(int)
    photos = orm.Set('Photo')

class Photo(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    url = orm.Required(str)
    owner = orm.Required(User)
    tags = orm.Set('Tag')

class Tag(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str)
    photos = orm.Set(Photo)


db.bind(provider='sqlite', filename='sqlite_database_pony.db', create_db=True)
db.generate_mapping(create_tables=True)
orm.set_sql_debug(True)
###################################
@orm.db_session
def fill_data():
    u1 = User(name='Alice', age=25)
    u2 = User(name='Bob', age=18)
    p1 = Photo(url='https://www.pinterest.com/pin/706080047826475767/', owner=u1)
    p2 = Photo(url='https://900913.ru/static/img/logo-192x192.png', owner=u2)
    p3 = Photo(url='https://900913.ru/static/img/9cover.jpg', owner=u2)
    orm.commit()

# fill_data()

@orm.db_session
def create_select_m2m():

    t1 = Tag(name='sql')
    t2 = Tag(name='linux')
    t3 = Tag(name='python')

    for p in orm.select(x for x in Photo):
        if p.id % 2:
            p.tags.add(t1)
            p.tags.add(t2)
        else:
            p.tags.add(t2)

    print(orm.select(p.url for p in Photo if t1 in p.tags)[:])
#
create_select_m2m()
# @orm.db_session
# def selct():
#
#
# selct()