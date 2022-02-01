# Kyle Gotzman 
# CSD 310 Database Dev and Use
# Module 9.3 Pysports Update and Delete
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

def display_players(cursor, title):
    #function to create inner join of player and team table

    #inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("\n-- {} --".format(title))
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

#connection test code
try:
    db = mysql.connector.connect(**config)

    #cursor
    cursor = db.cursor()

    #insert player and then display info
    add_new_player = ("INSERT INTO player(first_name, last_name, team_id)"
    "VALUES(%s, %s, %s)")
    player_info = ("Smeagol", "Shire Folk", 1)
    cursor.execute(add_new_player, player_info)
    db.commit()
    display_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    #update player and then display info
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    cursor.execute(update_player)
    display_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    #delete player and then display info
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute(delete_player)
    display_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

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