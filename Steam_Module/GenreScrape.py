import requests
from bs4 import BeautifulSoup

# MySQL connection Start
import mysql.connector

from Database import db_con

mydb = db_con()

# MySQL connection Stop

# MySQL Select Start
mycursor = mydb.cursor()

sql = 'select appid from steam_games where genre = "Empty"'
mycursor.execute(sql)
myresult = mycursor.fetchall()

mydb.commit()
# MySQL Select Stop

for appId in myresult:
    # URL PART Start
    URL = 'https://store.steampowered.com/app/' + str(appId[0])
    print(URL)
    page = requests.get(URL)
    data = BeautifulSoup(page.content, 'html.parser')
    # URL PART End

    # Genre scrape Start
    genre = data.find('div', {"id": "genresAndManufacturer"})

    if genre is not None:   # Failsafe for records like DLC which don't have webpage or at least genre tag.
        genre1 = genre.find('a')
        genre2 = str(genre1)
        genre2 = genre2.replace('</a>', '')

        genre_out2 = genre2.split('>')
        if genre2 != 'None':    # Failsafe for few edge cases that popped up while scraping with "genre = data.find('div', {"class": "details_block"})" kept as failsafe for other edge cases.
            genre3 = genre_out2[1]
            # Genre scrape Stop

            # MySQL insert steam_user_games_genre Start
            mycursor = mydb.cursor()
            sql = 'UPDATE steam_games SET genre="' + str(genre3) + '" where appid=' + str(appId[0])
            mycursor.execute(sql)
            mydb.commit()
            # MySQL insert steam_games_genre Stop
        else:
            # MySQL insert steam_user_games_genre Start
            mycursor = mydb.cursor()
            sql = 'UPDATE steam_games SET genre="Check" where appid=' + str(appId[0])
            mycursor.execute(sql)
            mydb.commit()
            # MySQL insert steam_games_genre Stop
    else:
        # MySQL update steam_user_games_genre Start
        mycursor = mydb.cursor()
        sql = 'UPDATE steam_games SET genre="None" where appid=' + str(appId[0])
        mycursor.execute(sql)
        mydb.commit()
        # MySQL update steam_games_genre Stop