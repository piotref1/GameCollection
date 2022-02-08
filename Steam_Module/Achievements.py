import requests
from bs4 import BeautifulSoup

# MySQL connection Start
from Database import db_con
mydb = db_con()
# MySQL connection Stop

# MySQL select Start
mycursor = mydb.cursor()
sql = "select id, profile_link, email from users"
mycursor.execute(sql)
user_list = mycursor.fetchall()
print(user_list)
mydb.commit()
# MySQL select Stop

for users in user_list:

    print(users)
    # Game List fetching start
    sql = "select usg.id, usg.game_id, has_achievements from user_steam_games usg join steam_games on usg.game_id = appid where usg.user_id = " + str(users[0]) + " and has_achievements=1"
    mycursor.execute(sql)
    game_list = mycursor.fetchall()
    print(game_list)
    # Game list fetching stop

    for games in game_list:
        # URL Part Start
        URL = 'https://steamcommunity.com/id/' + str(users[1]) + '/stats/' + str(games[1]) + '/?tab=achievements'
        page = requests.get(URL)
        data = BeautifulSoup(page.content, 'html.parser')
        # URL Part STOP

        # Achievements scrape Start
        achievements = data.find('meta', {"name": "Description"})
        mycursor = mydb.cursor()
        # Achievements scrape Stop

        # MySQL update steam_user_games achievements Start
        if achievements is None:
            sql = 'UPDATE user_steam_games usg SET achievements="0", achievements_percentage="0" where usg.id="' + str(games[0]) +'"'
        else:
            txt = str(achievements)
            txt = txt.replace('<meta content=', "")
            txt = txt.replace('achievements earned:" name="Description"/>', "")
            txt = txt.replace('"', "")
            txt = txt.replace('of', "")
            txt = txt.replace('(', "")
            txt = txt.replace('%)', "")
            x = txt.split(' ')

            sql = 'UPDATE user_steam_games usg SET achievements="' + str(x[0]) + '", achievements_percentage="' + str(
                x[3]) + '"' + ' where usg.id="' + str(games[0]) +'"'

        #print("user id:" + str(users[0]))
        # print(games[1])
        # print(x[3])

        mycursor.execute(sql)
        mydb.commit()
        # MySQL update steam_games achievements Stop
