import mysql.connector
from mysql.connector import errorcode

# CONNECT TO DB
def connect():
  # DATABASE CONFIG OBJ
  config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
  }

  # CONNECTION TEST CODE
  try:
    db = mysql.connector.connect(**config)
    return db
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

# VIEW BOOKS
def view_books(db):
    view_books_cursor = db.cursor()
    view_books_cursor.execute("SELECT book_name, author, details FROM book;")

    view_books_results = view_books_cursor.fetchall()

    for(book_name, author, details) in view_books_results:
      print("Book Name: {}, Author: {}\nDetails: {}\n\n".format(book_name, author, details))
    view_books_cursor.close()

    # RETURN TO MAIN MENU
    input('Press any key to return to the Main Menu')
    menu(db)

# STORE LOCATION
def store_locations(db):
    store_locator_cursor = db.cursor()
    store_locator_cursor.execute("SELECT store_id, locale FROM store;")

    store_locator_results = store_locator_cursor.fetchall()

    for(store_id, locale) in store_locator_results:
      print("Store ID: {}, Location: {}".format(store_id, locale))
    store_locator_cursor.close()


    # RETURN TO MAIN MENU
    input('Press any key to return to the Main Menu')
    menu(db)

# VIEW USER WISHLIST
def user_wishlist(db, user_id):
  user_wishlist_cursor = db.cursor()
  user_wishlist_cursor.execute("SELECT b.book_id, b.book_name, b.author, b.details FROM book AS b JOIN wishlist AS w on b.book_id = w.book_id WHERE w.user_id = {};".format(user_id))

  user_wishlist_results = user_wishlist_cursor.fetchall()

  for(book_id, book_name, author, details) in user_wishlist_results:
    print("Book ID: {}, Book Name: {}, Author: {}\nDetails: {}\n".format(book_id, book_name, author, details))

  user_wishlist_cursor.close()

  #TAKE USER TO ACCCOUNT MENU
  account_menu(db, user_id)

# ADD BOOK
def add_book(db, user_id):
  print("Add a book to your wishlist: \n")
  print("Books Available to be added: \n")

  # SHOW AVAILABLE BOOKS TO ADD
  view_books_cursor = db.cursor()
  view_books_cursor.execute("SELECT b.book_id, b.book_name, b.details, b.author FROM book AS b LEFT JOIN wishlist AS w ON b.book_id = w.book_id AND w.user_id ={} WHERE w.wishlist_id IS NULL;".format(user_id))

  view_books_results = view_books_cursor.fetchall()

  for(book_id, book_name, author, details) in view_books_results:
    print(f"Book ID: {book_id}, Book Name: {book_name}, Author: {author}\nDetails: {details}\n")

  # PROMPT USER TO SELECT A BOOK TO ADD TO THEIR WISHLIST
  user_book_selection = input("\nUsing the 'Book ID', please select which book you'd like to add to your wishlist: ")

  # CHECK BOOK TABLE TO ASSURE BOOK ID EXISTS
  check_book_id_cursor = db.cursor()
  check_book_id_cursor.execute("SELECT COUNT(book_id) FROM book WHERE book_id = {}".format(user_book_selection))
  check_book_id, = check_book_id_cursor.fetchone()

  if check_book_id == 0:
    print(" The user ID you selected was invalid, please try again.\n")
    input(" Press any key to continue...")
    add_book(db, user_id)

  elif check_book_id > 0:
    add_book_cursor = db.cursor()
    add_book_cursor.execute("INSERT INTO wishlist (user_id, book_id) VALUES ({}, {})".format(user_id, user_book_selection))
    db.commit()
    add_book_cursor.close()

    # TAKE USER TO ACCOUNT MENU
    account_menu(db, user_id)

# ACCOUNT MENU
def account_menu(db, user_id):

  print("\n Account Menu for User {}:\n Select '1' to View your Wishlist\n Select '2' to Add a book to your Wishlist\n Select '3' to return to the Main Menu\n".format(user_id))

  account_selection = input(' Selection: ')

  # VERIFY USER INPUT SELECTION
  if account_selection == '1':
    print(' View Wishlist\n')
    user_wishlist(db, user_id)

  if account_selection == '2':
    print(' Add a book to your Wishlist.\n')
    # INSERT FUNCTION
    add_book(db, user_id)

  if account_selection == '3':
    print(' You selected to return to the Main Menu.\n ')
    menu(db)

# MAIN ACCESS ACCOUNT FUNCTION
def access_account(db):
      # PROMPT USER TO ENTER THEIR user_id
    user_id_selection = input(' Select Your User ID: ')

    # QUERY
    user_id_cursor = db.cursor()
    user_id_cursor.execute("SELECT COUNT(user_id) FROM user WHERE user_id = {}".format(user_id_selection))
    check_user, = user_id_cursor.fetchone()

    # CHECK IF USER_ID IS VALID
    # INVALID USER
    if check_user == 0:
      print(" The User ID you selected was invalid, please try again.\n")
      input(" Press any key to continue...\n")
      main()

    # VALID USER
    elif check_user > 0:
      print(" Login Successful! Welcome User {}!".format(user_id_selection))

      account_menu(db, user_id_selection)

# MAIN MENU
def menu(db):
  print(' WhataBook Menu, please make a selection:\n\n Select 1 for "View Books" \n Select 2 for "View Store Locators" \n Select 3 for "My Account" \n Select 4 to "Exit"\n')

  menu_selection = input(" Selection: ")

  # CHECK MENU SELECTION BLOCK

  if menu_selection == '1':
    view_books(db)

  # VIEW STORE LOCATORS
  elif menu_selection == '2':
    store_locations(db)

  # MY ACCOUNT
  elif menu_selection == '3':
    access_account(db)

  # EXIT
  elif menu_selection == '4':
    print('\nThanks for using WhataBook, Goodbye!')
    exit()

# MAIN PROGRAM
def main():
  # CONNECT TO DB
  db = connect()

  # USER MENU
  menu(db)


main()
