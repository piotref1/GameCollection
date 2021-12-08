# MySQL connection Start
import random

import mysql.connector

# MySQL select Start
from Database import db_con, genre_based_game_fetch

mydb = db_con()
mycursor = mydb.cursor()

sql = "select id from users"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(myresult)
mydb.commit()
# MySQL select Stop

for user_id in myresult:

    # MySQL select count of genres Start
    sql = "select usg.user_id, genre, count(*) from user_steam_games usg join steam_games on usg.game_id=appid where usg.user_id=" + str(user_id[0]) + " and genre!='None' group by genre order by count(*) DESC"
    mycursor.execute(sql)
    users_genre_count = mycursor.fetchall()
    # MySQL select count of genres Stop

    # Selecting random games from the list START
    game_suggestion = genre_based_game_fetch(users_genre_count[0][1], str(user_id[0]), 3) + genre_based_game_fetch(users_genre_count[1][1], str(user_id[0]), 1) + genre_based_game_fetch(users_genre_count[2][1], str(user_id[0]), 1)
    # Selecting random games from the list START

    # Deleting from DB to not double records or have to update over START
    sql = "delete from user_steam_recommended_games usrg where usrg.user_id=" + str(user_id[0])
    mycursor.execute(sql)
    # Deleting from DB to not double records or have to update over STOP

    # Insert into user_steam_recommended_games_buy Start
    sql = "insert into user_steam_recommended_games(user_id, game_id, type) values (" + str(user_id[0]) + ",%s,'Buy')"
    mycursor.executemany(sql, game_suggestion)
    mydb.commit()
    # Insert into user_steam_recommended_games_buy Stop

    # MySQL select list of games to finish Start
    sql = "select game_id from user_steam_games usg join steam_games sg on usg.game_id=sg.appid where usg.user_id = " + str(
        user_id[
            0]) + " and achievements_percentage<100 and achievements_percentage>70 order by achievements_percentage DESC;"
    mycursor.execute(sql)
    users_to_finish_game_list = mycursor.fetchall()

    # MySQL select list of games to finish Stop
    game_list = random.sample(users_to_finish_game_list, 3)

    # Insert list of games to finish into user_steam_recommended_games Start
    sql = "insert into user_steam_recommended_games(user_id, game_id, type) values (" + str(
        user_id[0]) + ",%s,'Finish')"
    mycursor.executemany(sql, game_list)
    mydb.commit()
    # Insert list of games to finish into user_steam_recommended_games Stop

    # MySQL select list of games to play Stop
    sql = "select game_id from user_steam_games usg join steam_games sg on usg.game_id=sg.appid where usg.user_id = " + str(
        user_id[
            0]) + " and achievements_percentage<70 order by achievements_percentage DESC;"
    mycursor.execute(sql)
    users_to_play_game_list = mycursor.fetchall()
    print(users_to_play_game_list)
    # MySQL select list of games to play Stop

    game_list = random.sample(users_to_play_game_list, 5)
    # Insert list of games to play into user_steam_recommended_games Start
    sql = "insert into user_steam_recommended_games(user_id, game_id, type) values (" + str(
        user_id[0]) + ",%s,'Play')"
    mycursor.executemany(sql, game_list)
    mydb.commit()
    # Insert list of games to play into user_steam_recommended_games Stop


