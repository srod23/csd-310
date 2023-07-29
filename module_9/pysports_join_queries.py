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

    def join_queries():
      join_cursor = db.cursor()
      join_cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
      join_result = join_cursor.fetchall()

      for (player_id, first_name, last_name, team_name) in join_result:
        print("Player ID: {} \nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player_id, first_name, last_name, team_name))
      join_cursor.close()

    # Print Results from Inner Join
    print('-- DISPLAYING PLAYER RECORDS --')
    join_queries()

    input("\n\n Press any key to continue...")

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
