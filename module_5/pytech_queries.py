# Kyle Gotzman
# CSD 310 Database Dev and Use
# Module 5.3 Queries
# 11/13/2021

# import
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.gd2jy.mongodb.net/pytech"

# connect to MongoDB and pytech db
client = MongoClient(url)
db = client.pytech 

# retrieve students collection
students =db.students

# find students in the collection
student_list =students.find({})

# display message 
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# create for loop and output results
for doc in student_list:
    print("   Student ID: " + doc["student_id"] + "\n   First Name: " + doc["first_name"] + "\n   Last Name: " + doc["last_name"] + "\n")

# find document by student_id
jannet = students.find_one({"student_id": "1008"})

# output results
print("\n -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("   Student ID: " + jannet["student_id"] + "\n   First Name: " + jannet["first_name"] + "\n   Last Name: " + jannet["last_name"] + "\n")

# exit message
input("\n\n End of program, press any key to continue...") 