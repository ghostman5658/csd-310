# Kyle Gotzman
# CSD 310 Database Dev and Use
# Module 5
# 11/13/2021

# import
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.gd2jy.mongodb.net/pytech"

# connect to MongoDB and pytech db
client = MongoClient(url)
db = client.pytech

# display connected collections
print("\n -- Pytech COllection List --")
print(db.list_collection_names())

# display exit message
input("\n\n End of program, press any key to exit... ")