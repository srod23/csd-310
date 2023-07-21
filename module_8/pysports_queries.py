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

    def team_queries():
      team_cursor = db.cursor()
      team_cursor.execute("SELECT team_id, team_name, mascot FROM team")
      team_result = team_cursor.fetchall()

      for (team_id, team_name, mascot) in team_result:
        print("Team ID: {} \nTeam Name: {}\nMascot: {}\n".format(team_id, team_name, mascot))
      team_cursor.close()

    # Print Results from Team
    print('-- DISPLAYING TEAM RECORDS --')
    team_queries()

    def player_queries():
      player_cursor = db.cursor()
      player_cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
      player_result = player_cursor.fetchall()

      for (player_id, first_name, last_name, team_id) in player_result:
        print("Player ID: {} \nFirst Name: {}\nLast Name: {}\nTeam ID:{} \n".format(player_id, first_name, last_name, team_id))
      player_cursor.close()

    # Print Results from Team
    print('-- DISPLAYING PLAYER RECORDS --')
    player_queries()

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
