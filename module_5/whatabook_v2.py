# Kyle Gotzman 
# CSD 310 Database Dev and Use
# Module 12.3 Whatabook program
# 12/11/2021

#import statements
import sys
import mysql.connector
from mysql.connector import errorcode

#database config object
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# Method for main menu that returns users menu selection 
def show_menu():
    print("\nWELCOME TO THE WHATABOOK ONLINE LIBRARY!")
    print("\n   --  Main Menu  --   ")
    print("\n   1. View Books")
    print("   2. View Store Locations")
    print("   3. My Account")
    print("   4. Exit Program")
    user_selection = input("\nPlease select from one of the above items: ")
    try:
        return int(user_selection)
    
    except ValueError:
        None

# Method that queries database and displays books
def show_books(_cursor):
    # query database and join table
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    book_inventory = _cursor.fetchall()

    # Display available books
    print("   --  Available Books  --   ")
    for book in book_inventory:
        print("Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2]))

# Method that queries database and displays store locations
def show_locations(_cursor):
    # query database and join table
    _cursor.execute("SELECT store_id, locale FROM store")
    store_locations = _cursor.fetchall()

    # Display available locations
    for location in store_locations:
        print("\nStore Address: {}\n".format(location[1]))

# Method used to validate user (user_id must be 1, 2, or 3)
def validate_user():
    user_id = input("Please enter your USER ID: ")
    try:
        return int(user_id)
    except ValueError:
        None

# Method for displaying user account menu and prompting user for input/selection
def show_account_menu():
    print("\n   --  Account Options  --   ")
    print("\n   1. Wishlist")
    print("   2. Add Book")
    print("   3. Main Menu")
    account_selection = input("\nPlease select from one of the above options: ")
    try:
        return int(account_selection)
    except ValueError:
        None

# Method that queries the database and displays the users wishlist
def show_wishlist(_cursor, _user_id):
    # query database and join table
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
        "FROM wishlist " +
        "INNER JOIN user ON wishlist.user_id = user.user_id " +
        "INNER JOIN book ON  wishlist.book_id = book.book_id " +
        "WHERE user.user_id = {}".format(_user_id))
    user_wishlist = _cursor.fetchall()

    # display user wishlist
    print("\n   --  Your Current Wishlist Items Are  --   ")
    for book in user_wishlist:
        print("\nBook Name: {}\nAuthor: {}\nBook ID: {}\n".format(book[4], book[5], book[3]))

# Method that displays books not in the users wishlist that can be added
def show_books_to_add(_cursor, _user_id):
    # query database and join table
    _cursor.execute("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    potential_wishlist_books = _cursor.fetchall()

    # display additional books that can be added to the user wishlist
    print("\n   --  Books That Can Be Added To Your Wishlist  --   ")
    for book in potential_wishlist_books:
        print("\nBook ID: {}\nBook Name: {}".format(book[0], book[1]))

# Method for adding / inserting a book into a users wishlist
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

# Initiate program and connect to whatabook database
try:
    db = mysql.connector.connect(**config)
    #cursor
    cursor = db.cursor()

    # Call main menu method 
    main_menu_selection = show_menu()

    # initiate while loop to keep program running until user selects option 4
    while main_menu_selection != 4:

        # If main menu selection is 1, call the show_books method
        if main_menu_selection == 1:
                show_books(cursor)

        # If main menu selection is 2, call the show_locations method
        if main_menu_selection == 2:
            show_locations(cursor) 

        # If main menu selection is 3, validate user with validate_user method and then call show_account_menu method to prompt user input
        if main_menu_selection == 3:

            selected_user_id = validate_user()
            while selected_user_id != 1 and selected_user_id != 2 and selected_user_id != 3:
                print("Invalid User ID")
                print("Please try again")
                selected_user_id = validate_user()

            selected_account_option = show_account_menu()

            # initiate while loop that keeps user in account menu until exit or main menu selection
            while selected_account_option != 3:

                if selected_account_option == 1:
                    show_wishlist(cursor, selected_user_id)

                if selected_account_option == 2:
                    show_books_to_add(cursor, selected_user_id)
                    book_id = int(input("\nEnter the book ID you want to add: "))
                    add_book_to_wishlist(cursor, selected_user_id, book_id)
                    db.commit()
                    print("\nBook ID: {} was added to your wishlist".format(book_id))

                if selected_account_option == 3:
                    show_menu()

                if selected_account_option != 1 and selected_account_option != 2 and selected_account_option != 3:
                    print("\nInvalid Selection")
                    print("Please try again")

                # change selected account option variable to avoid forever loop
                selected_account_option = show_account_menu()

        if main_menu_selection == 4:
            print("\nThank you for visiting WhatABook online library")
            print("The program will now exit...")
            sys.exit(0)

        if main_menu_selection != 1 and main_menu_selection != 2 and main_menu_selection != 3 and main_menu_selection != 4:
            print("\nInvalid selection")
            print("Please try again")

        # change main menu variable back to default to avoid forever loop
        main_menu_selection = show_menu()

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