# Kyle Gotzman 
# CSD 310 Database Dev and Use
# Module 9.2 Pysports Join Queries
# 12/3/2021

#import statements
import mysql.connector
from mysql.connector import errorcode

#database config object
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#connection test code
try:
    db = mysql.connector.connect(**config)

    #cursor
    cursor = db.cursor()

    #inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()

    #display player records
    print("\n-- DISPLAYING PLAYER RECORDS --")

    #for loop for team table
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\nPress any key to continue... ")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or passoword are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

#exit
finally:
    db.close() 