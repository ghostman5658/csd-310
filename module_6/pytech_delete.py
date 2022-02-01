# Kyle Gotzman
# CSD 310 Database Dev and Use
# Module 6.3 Pytech Delete
# 11/17/2021

#import
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.gd2jy.mongodb.net/pytech"

#connect to the MongoDB cluster and pytech database
client = MongoClient(url)
db = client.pytech 

#get students collection
students = db.students

#find students
student_list = students.find({}) 

#display message 
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#create for loop and display records 
for doc in student_list:
    print("Student ID: " + doc["student_id"] + 
    "\nFirst Name: " + doc["first_name"] + 
    "\nLast Name: " + doc["last_name"] + "\n")

#insert new record
new_record_id = students.insert_one({"student_id": "1010", "first_name": "Kyle", "last_name": "Gotzman"}).inserted_id

#display message
print("\n-- INSERT STATEMENTS --")
print("Inserted student record into students collection with document_id" + str(new_record_id))

#call the find_one method by student_id 1010
new_record_doc = students.find_one({"student_id": "1010"})

#display inserted record doc
print("\n-- DISPLAYING STUDENT TEST DOC --")
print("Student ID: " + new_record_doc["student_id"] +
"\nFirst Name: " + new_record_doc["first_name"] + 
"\nLast Name: " + new_record_doc["last_name"] + "\n")

#call the delete_one method by student_id 1010
deleted_new_record_doc = students.delete_one({"student_id": "1010"})

#call the find method and display results to terminal window
student_list_new = students.find({})
print("\n-- DISPLAYING STUDENTS FROM find() QUERY --")
for docs in student_list_new:
    print("Student ID: " + docs["student_id"] +
    "\nFirst Name: " + docs["first_name"] +
    "\nLast Name: " + docs["last_name"] + "\n")

# end program
print("End of program, press any key to continue...") 