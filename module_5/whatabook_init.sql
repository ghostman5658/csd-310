-- Kyle Gotzman
-- Database and Dev
-- Whatabook Init 

-- drop user if exists
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop constraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

-- create tables

CREATE TABLE store (
    store_id        INT             NOT NULL    AUTO_INCREMENT,
    locale          VARCHAR(500)    NOT NULL,
    PRIMARY KEY (store_id)
);

CREATE TABLE book (
    book_id         INT             NOT NULL    AUTO_INCREMENT,
    book_name       VARCHAR(200)    NOT NULL,
    author          VARCHAR(200)    NOT NULL,
    details         VARCHAR(500),
    PRIMARY KEY (book_id)
);

CREATE TABLE user (
    user_id         INT             NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75)     NOT NULL,
    last_name       VARCHAR(75)     NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE wishlist (
    wishlist_id     INT             NOT NULL    AUTO_INCREMENT,
    user_id         INT             NOT NULL,
    book_id         INT             NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
);

-- insert store record(s)

INSERT INTO store(locale)
    VALUES('130 Porch Swing Way, Holly Ridge, NC 28445');

-- insert book record(s)
INSERT INTO book(book_name, author, details)
    VALUES('A Game of Thrones', 'George R.R. Martin', 'The first book of the Game of Thrones series');

INSERT INTO book(book_name, author, details)
    VALUES('A Clash of Kings', 'George R.R. Martin', 'The second book of the Game of Thrones series');

INSERT INTO book(book_name, author, details)
    VALUES('A Storm of Swords 1. Steel and Snow', 'George R.R. Martin', 'The first part of the third book of the Game of Thrones series');

INSERT INTO book(book_name, author, details)
    VALUES('A Storm of Swords 2. Blood and Gold', 'George R.R. Martin', 'The second part of the third book of the Game of Thrones series');

INSERT INTO book(book_name, author, details)
    VALUES('A Feast For Crows', 'George R.R. Martin', 'The fourth book of the Game of Thrones series');

INSERT INTO book(book_name, author, details)
    VALUES('A Dance with Dragons 1. Dreams and Dust', 'George R.R. Martin', 'The first part of the fifth book of the Game of Thrones series');

INSERT INTO book(book_name, author, details)
    VALUES('A Dance with Dragons 2. After the Feast', 'George R.R. Martin', 'The second part of the fifth book of the Game of Thrones series');

INSERT INTO book(book_name, author, details)
    VALUES('The Winds of Winter', 'George R.R. Martin', 'The sixth book of the Game of Thrones series');

INSERT INTO book(book_name, author, details)
    VALUES('A Dream of Spring', 'George R.R. Martin', 'The seventh book of the Game of Thrones series');

-- insert user record(s)
INSERT INTO user(first_name, last_name)
    VALUES('John', 'Snow');

INSERT INTO user(first_name, last_name)
    VALUES('Sansa', 'Stark');

INSERT INTO user(first_name, last_name)
    VALUES('Tyrion', 'Lanister');

-- insert wishlist record(s)
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'),
        (SELECT book_id FROM book WHERE book_name = 'A Storm of Swords 2. Blood and Gold')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Sansa'),
        (SELECT book_id FROM book WHERE book_name = 'A Clash of Kings')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Tyrion'),
        (SELECT book_id FROM book WHERE book_name = 'A Game of Thrones')
    );
