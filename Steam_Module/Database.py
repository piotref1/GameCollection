import random


def db_con():

    # MySQL connection Start
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="steam"
    )
    return mydb
    # MySQL connection Stop


def genre_based_game_fetch(fetched_genre, user_id_fetch, amount):
    # Turn this into function #
    mydb = db_con()
    mycursor = mydb.cursor()
    sql = "select appid from steam_games where genre='" + str(fetched_genre) + "' and appid not in (select game_id from user_steam_games where user_id=" + str(user_id_fetch) + " and game_id=appid)"
    mycursor.execute(sql)
    list_of_games_not_in_user_collection = mycursor.fetchall()
    # returns random.sample(list_of_games_not_in_user_collection, x)

    game_list = random.sample(list_of_games_not_in_user_collection, amount)

    return game_list
