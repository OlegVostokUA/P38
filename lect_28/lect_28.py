# lect_28_ORM systems
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, \
    String, DateTime, ForeignKey, Numeric, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# engine = create_engine('mysql+pymysql://admin:password@localhost/my_database')
from sqlalchemy.orm import relationship, Session

engine = create_engine('sqlite:///sqlite_database.db')
session = Session(bind=engine)
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer())


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    line_items = relationship("OrderLine", backref='order')


class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    item_id = Column(Integer, ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship("Item")


Base.metadata.create_all(engine)













# user_post = Table('user_post', Base.metadata,
#                 Column('user_id', Integer(), ForeignKey('users.id')),
#                 Column('post_id', Integer(), ForeignKey('posts.id'))
#                   )
#
#
# # OO mapping
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer)
#     username = Column(String(20), nullable=False)
#     email = Column(String(50))
#     password = Column(String(16), nullable=False)
#     posts = relationship('Post', uselist=False)
#
#     __table_args__ = (
#         PrimaryKeyConstraint('id'),
#         UniqueConstraint('username')
#     )
#
#
# class Post(Base):
#     __tablename__ = 'posts'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     title = Column(String(50), nullable=False)
#     content = Column(String(200), nullable=False)
#     slug = Column(String(50), nullable=False, unique=True)
#     created_on = Column(DateTime(), default=datetime.now)
#     updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
#
# # Base.metadata.create_all(engine)
#
# Base.metadata.drop_all(engine)
















## classic mapping
# metadata = MetaData()
#
# post = Table('posts', metadata,
#              Column('id', Integer(), primary_key=True),
#              Column('slug', String(200), nullable=False, unique=True))
#
# class Post(object):
#     pass
#
# from sqlalchemy.orm import mapper
# mapper(Post, post)