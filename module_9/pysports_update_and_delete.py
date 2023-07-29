import mysql.connector
from mysql.connector import errorcode

# Databse Config Object


config = {
    "user": "root",
    "password": "password",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


# Connection Test Code
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with databse {}".format(
        config["user"], config["host"], config["database"]))

    # INSERT NEW PLAYER
    def insert():
      insert_cursor = db.cursor()

      insert_cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES ('Ginny', 'Weasley', 1);")

      insert_cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")

      insert_result = insert_cursor.fetchall()

      for (player_id, first_name, last_name, team_name) in insert_result:
        print("Player ID: {} \nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player_id, first_name, last_name, team_name))

      insert_cursor.close()

    # PRINT RESULTS AFTER INSERT NEW PLAYER
    print('-- DISPLAYING PLAYER RECORDS AFTER INSERT--')
    insert()

    input("\n\n Press any key to continue...")

    # UPDATE NEW PLAYER TO TEAM_ID 2
    def update():
        update_cursor = db.cursor()

        update_cursor.execute("UPDATE player SET team_id = 2, first_name = 'Ginny', last_name = 'Weasley' WHERE first_name = 'Ginny';")

        update_cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id WHERE first_name = 'Ginny';")

        update_result = update_cursor.fetchall()

        for (player_id, first_name, last_name, team_name) in update_result:
         print("Player ID: {} \nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player_id, first_name, last_name, team_name))

        update_cursor.close()

    # PRINT RESULTS AFTER UPDATE NEW PLAYER
    print('-- DISPLAYING PLAYER RECORDS AFTER UPDATE--')
    update()

    input("\n\n Press any key to continue...")

    # DELETE UPDATED PLAYER
    def delete():
      delete_cursor = db.cursor()

    #   DELETE NEW PLAYER
      delete_cursor.execute("DELETE FROM player WHERE first_name = 'Ginny';")
      delete_cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
      delete_result = delete_cursor.fetchall()

      for (player_id, first_name, last_name, team_name) in delete_result:
        print("Player ID: {} \nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player_id, first_name, last_name, team_name))

      delete_cursor.close()

    # Print Results from DELETE
    print('-- DISPLAYING PLAYER RECORDS AFTER DELETE--')
    delete()

    # input("\n\n Press any key to continue...")

    db.close()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    db.close()
    print('Database Closed.')
