import pymongo

my_client = pymongo.MongoClient('mongodb://localhost:27017')

my_db = my_client['my_database']

my_col = my_db['customers']

# my_dict = {'name': 'John', 'address': 'Highway 37'}
# my_dict = {'s_name': 'Bob', 'email': 'eeeee@gmail.com', 'age': '55'}

my_list = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = my_col.insert_many(my_list)

# x = my_col.find_one()
# query = {'address': 'Park Lane 38'}
# query_1 = {'_id': 0, 'name': 1, 'address': 1}
#
# x = my_col.find(query)
#
# for i in x:
#     print(i)
# for i in my_col.find():
#     print(i, type(i))

# query = {'address': 'Green Grass 1'}
# new_val = {'$set': {'address': 'Vxred 9999'}}
#
# s = my_col.update_one(query, new_val)
#
# for i in my_col.find():
#     print(i)
#
# print(s.modified_count)



# query = {'address': {'$regex': '^O'}}
#
# x = my_col.delete_many(query)
#
# for i in my_col.find():
#     print(i)
#
# print(x.deleted_count, 'deleted')

