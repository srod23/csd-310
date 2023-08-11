import mysql.connector
from mysql.connector import errorcode

# Configuration settings for your MySQL server
config = {
    "user": "root",  # Change to your MySQL user
    "password": "password",  # Change to your MySQL password
    "host": "127.0.0.1",
}

# SQL commands to create the required database and tables
DB_NAME = "whatabook"

TABLES = {
    'user': """
        CREATE TABLE `user` (
            `user_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `first_name` VARCHAR(75) NOT NULL,
            `last_name` VARCHAR(75) NOT NULL
        ) ENGINE=InnoDB
    """,

    'book': """
        CREATE TABLE `book` (
            `book_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `book_name` VARCHAR(200) NOT NULL,
            `details` VARCHAR(500),
            `author` VARCHAR(200) NOT NULL
        ) ENGINE=InnoDB
    """,

    'store': """
        CREATE TABLE `store` (
            `store_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `locale` VARCHAR(500) NOT NULL
        ) ENGINE=InnoDB
    """,

    'wishlist': """
        CREATE TABLE `wishlist` (
            `wishlist_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `user_id` INT NOT NULL,
            `book_id` INT NOT NULL,
            FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`),
            FOREIGN KEY (`book_id`) REFERENCES `book`(`book_id`)
        ) ENGINE=InnoDB
    """
}
INSERTS = {
    'store': "INSERT INTO store (locale) VALUES ('San Antonio')",
    'user': """
        INSERT INTO user (first_name, last_name) VALUES
        ('John', 'Doe'),
        ('Jane', 'Doe'),
        ('John', 'Smith')
    """,
    'book': """
        INSERT INTO book (book_name, author, details) VALUES
        ('Harry Potter and the Sorcerers Stone', '"Harry Potter is the boy who lived"', 'J.K. Rowling'),
        ('Harry Potter and the Chamber of Secrets ', '“Albus Dumbledore is the greatest sorcerer in the world.”', 'J.K. Rowling'),
        ('Harry Potter and the Prisoner of Azkaban', '"I’m not doing this for you. I’m doing it because – I don’t reckon my dad would’ve wanted them to become killers – just for you."', 'J.K. Rowling'),
        ('Harry Potter adn the Goblet of Fire', '“Numbing the pain for a while will make it worse when you finally feel it.”', 'J.K. Rowling'),
        ('Harry Potter and the Order of the Phoenix', '"Harry Potter is the boy who lived"', 'J.K. Rowling'),
        (' Harry Potter and the Half-Blood Prince', '“It is the unknown we fear when we look upon death and darkness, nothing more.”', 'J.K Rowling'),
        ('Harry Potter and the Deathly Hallows', '“Do not pity the dead, Harry, pity the living, and above all those who live without love.”', 'J.K. Rowling'),
        ('Harry Potter and the Cursed Child', '"How to distract Scorpius from difficult emotional issues. Take him to a library."', 'J.K. Rowling'),
        ('A Game of Thrones', 'Never forget what you are, for surely the world will not. Make it your strength. Then it can never be your weakness. Armor yourself in it, and it will never be used to hurt you.', 'George R.R. Martin')
    """
}

# Connect to the MySQL server
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Create the 'whatabook' database
try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        cursor.execute("CREATE DATABASE {}".format(DB_NAME))
        cursor.execute("USE {}".format(DB_NAME))
    else:
        print(err)
        exit(1)

# Create the tables inside 'whatabook' database
for table_name, table_sql in TABLES.items():
    try:
        print(f"Creating table {table_name} ...", end="")
        cursor.execute(table_sql)
        print("Done.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print(f"Table {table_name} already exists.")
        else:
            print(err)
# Insert specified records
for table_name, insert_sql in INSERTS.items():
    try:
        print(f"Inserting into {table_name} ...", end="")
        cursor.execute(insert_sql)
        conn.commit()  # Commit the insertion
        print("Done.")
    except mysql.connector.Error as err:
        print(err)
# Clean up
cursor.close()
conn.close()
