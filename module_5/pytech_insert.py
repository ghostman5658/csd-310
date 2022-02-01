# Kyle Gotzman
# CSD 310 Database Dev and Use
# Module 5.3 Insert Document
# 11/13/2021

# import
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.gd2jy.mongodb.net/pytech"

# connect to MongoDB and pytech db
client = MongoClient(url)
db = client.pytech

""" three student documents """
# John Smith's document
john = {
    "student_id": "1007",
    "first_name": "John",
    "last_name": "Smith",
    "enrollments": [
        {
            "term": "Q2",
            "gpa": 3.8,
            "start_date": "07/10/2021",
            "end_date": "09/14/2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Tracy Shelansky",
                    "grade": "A"
                },
                {
                   "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Darrel Payne",
                    "grade": "A" 
                }
            ]
        }
    ]
}
# Jannet Jackson's document
jannet = {
    "student_id": "1008",
    "first_name": "Jannet",
    "last_name": "Jackson",
    "enrollments": [
        {
            "term": "Q2",
            "gpa": 4.0,
            "start_date": "07/10/2021",
            "end_date": "09/14/2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Tracy Shelansky",
                    "grade": "A+"
                },
                {
                   "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Darrel Payne",
                    "grade": "A+" 
                }
            ]
        }
    ]
}
# Amy Wilson's document
amy = {
    "student_id": "1009",
    "first_name": "Amy",
    "last_name": "Wilson",
    "enrollments": [
        {
            "term": "Q2",
            "gpa": 3.0,
            "start_date": "07/10/2021",
            "end_date": "09/14/2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Tracy Shelansky",
                    "grade": "B"
                },
                {
                   "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Darrel Payne",
                    "grade": "B" 
                }
            ]
        }
    ]
}

# student collection
students = db.students

# insert documents and print statement
print("\n -- Insert Statements --")

john_student_id = students.insert_one(john).inserted_id
print(" Inserted student record John Smith into the students collection with document_id" + str(john_student_id))

jannet_student_id = students.insert_one(jannet).inserted_id
print(" Inserted student record Jannet Jackson into the students collection with document_id" + str(jannet_student_id))

amy_student_id = students.insert_one(amy).inserted_id
print(" Inserted student record Amy Wilson into the students collection with document_id" + str(amy_student_id)) 

input("\n\n End of program, press any key to exit... ")
