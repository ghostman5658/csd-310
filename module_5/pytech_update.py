# Kyle Gotzman 
# CSD 310 Database Dev and Use
# Module 6.2 Pytech Update
# 11/16/2021

# import
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.gd2jy.mongodb.net/pytech"

# connect to the MongoDB cluster and pytech database
client = MongoClient(url)
db = client.pytech

# get students collection
students = db.students

# find students
student_list = students.find({})

# display message
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# create for loop and display records
for doc in student_list:
    print("Student ID: " + doc["student_id"] + 
    "\nFirst Name: " + doc["first_name"] + 
    "\nLast Name: " + doc["last_name"] + "\n")

# update student_id 1007 to Smith II
db.students.update_one({
    "student_id": "1007"
},
{"$set":
{
    "last_name": "Smith II"
}})

# find one method for updated doc
updated_john = students.find_one({"student_id": "1007"})

# print display heading
print("\n-- DISPLAYING STUDENT DOCUMENT 1007 --")

# print updated student record
print("Student ID: " + updated_john["student_id"] +
"\nFirst Name: " + updated_john["first_name"] + 
"\nLast Name: " + updated_john["last_name"] + "\n")

# exit prompt
print("\nEnd of program, press any key to continue...")