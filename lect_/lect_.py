import sqlite3 as sq

conn = sq.connect('database.db')

with open('shema.sql') as f:
    conn.executescript(f.read())




##########################
# def create_db():
#     global base, cursor
#     base = sq.connect('test_db.db')
#     cursor = base.cursor()
#
#     sql_query = """CREATE TABLE IF NOT EXISTS Students(
#                     name TEXT, s_name TEXT, age INT,
#                      date_s DATE, group_n TEXT, grants INT)"""
#
#     cursor.execute(sql_query)
#
# create_db()
#
# def insert_db():
#     # base = sq.connect('test_db.db')
#     # cursor = base.cursor()
#
#     sql_query = """
#     INSERT INTO Students(name, s_name, age, date_s, group_n, grants)
#     VALUES
#     ('Джеймс', 'Хант', 28, '2012-08-21', 'B', 1200),
#     ('Ніккі', 'Лауда', 25, '2011-05-22', 'A', 1300),
#     ('Артур', 'Сенна', 22, '2013-04-23', 'B', 1500),
#     ('Міхаель', 'Шумахер', 25, '2016-07-24', 'A', 1800),
#     ('Кен', 'Блок', 35, '2010-02-35', 'B', 2500),
#     ('Коллін', 'Макрей', 21, '2017-10-26', 'A', 2200);
#     """
#     cursor.execute(sql_query)
#     base.commit()
#
# # insert_db()
#
# # def db_work():
# #
# #     # name = 'Джеймс'
# #     # s_name = 'Хант'
# #     name = (input(),)
# #     s_name = (input(),)
# #     val = name + s_name
# #
# #     # sql_query_2 = """SELECT * FROM Students
# #     #                     WHERE name == 'Джеймс' AND s_name == 'Хант'"""
# #     # sql_query_2 = f"""SELECT * FROM Students
# #     #                     WHERE name == '{name}' AND s_name == '{s_name}'"""
# #
# #
# #     sql_query_2 = """SELECT * FROM Students
# #                      WHERE name == ? AND s_name == ?"""
# #
# #     cursor.execute(sql_query_2, val)
# #
# #     records = cursor.fetchall()
# #     for i in records:
# #         print(i)
# #
# # db_work()
#
# new_p = [('Кенyy', 'Майлзff', 45, '2002-08-21', 'V', 7800), ('Льюіс', 'Хемільтон', 28, '2001-02-28', 'B', 6500)]
#
#
# def db_work(new):
#     sql_query_1 = """INSERT INTO Students VALUES (?,?,?,?,?,?)"""
#     cursor.executemany(sql_query_1, new)
#     base.commit()
#
#     sql_query_2 = """SELECT * FROM Students"""
#     cursor.execute(sql_query_2)
#     records = cursor.fetchall()
#     for i in records:
#         print(i)
#
# db_work(new_p)