# Kyle Gotzman 
# CSD 310 Database Dev and Use
# Module 8.3 Pysports Queries
# 11/23/2021

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
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall()

    #display team records
    print("\n-- DISPLAYING TEAM RECORDS --")

    #for loop for team table
    for team in teams:
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))

    #cursor
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()

    #display player records
    print("\n-- DISPLAYING PLAYER RECORDS --")

    #for loop for player table
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))
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