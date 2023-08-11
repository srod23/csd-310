-- Drop Database if exists 
DROP DATABASE IF EXISTS whatabook;

-- Create the 'whatabook' database
CREATE DATABASE IF NOT EXISTS whatabook;

-- Create a new user 'whatabook_user' with password 'MySQL8IsGreat!'
CREATE USER IF NOT EXISTS 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- Grant all privileges to 'whatabook_user' for the 'whatabook' database
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

USE whatabook;

-- Create the 'user' table
CREATE TABLE IF NOT EXISTS `user` (
    `user_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(75) NOT NULL,
    `last_name` VARCHAR(75) NOT NULL
) ENGINE=InnoDB;

-- Create the 'book' table
CREATE TABLE IF NOT EXISTS `book` (
    `book_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `book_name` VARCHAR(200) NOT NULL,
    `details` VARCHAR(500),
    `author` VARCHAR(200) NOT NULL
) ENGINE=InnoDB;

-- Create the 'store' table
CREATE TABLE IF NOT EXISTS `store` (
    `store_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `locale` VARCHAR(500) NOT NULL
) ENGINE=InnoDB;

-- Create the 'wishlist' table
CREATE TABLE IF NOT EXISTS `wishlist` (
    `wishlist_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT NOT NULL,
    `book_id` INT NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`),
    FOREIGN KEY (`book_id`) REFERENCES `book`(`book_id`)
) ENGINE=InnoDB;

-- Insert into the 'store' table
INSERT INTO store (locale) VALUES ('San Antonio');

-- Insert into the 'user' table
INSERT INTO user (first_name, last_name) VALUES
('John', 'Doe'),
('Jane', 'Doe'),
('John', 'Smith');

-- Insert into the 'book' table
INSERT INTO book (book_name, author, details) VALUES
('Harry Potter and the Sorcerers Stone', 'J.K. Rowling', 'Harry Potter is the boy who lived'),
('Harry Potter and the Chamber of Secrets', 'J.K. Rowling', '“Albus Dumbledore is the greatest sorcerer in the world.”'),
('Harry Potter and the Prisoner of Azkaban', 'J.K. Rowling', '"I’m not doing this for you. I’m doing it because – I don’t reckon my dad would’ve wanted them to become killers – just for you."'),
('Harry Potter adn the Goblet of Fire', 'J.K. Rowling', '“Numbing the pain for a while will make it worse when you finally feel it.”'),
('Harry Potter and the Order of the Phoenix', 'J.K. Rowling', '"Harry Potter is the boy who lived"'),
('Harry Potter and the Half-Blood Prince', 'J.K Rowling', '“It is the unknown we fear when we look upon death and darkness, nothing more.”'),
('Harry Potter and the Deathly Hallows', 'J.K. Rowling', '“Do not pity the dead, Harry, pity the living, and above all those who live without love.”'),
('Harry Potter and the Cursed Child', 'J.K. Rowling', '"How to distract Scorpius from difficult emotional issues. Take him to a library."'),
('A Game of Thrones', 'George R.R. Martin', 'Never forget what you are, for surely the world will not. Make it your strength. Then it can never be your weakness. Armor yourself in it, and it will never be used to hurt you.');
