import requests
from bs4 import BeautifulSoup

from Database import db_con
from ParentControlEmail import test_parent


# MySQL select Start
mydb = db_con()
mycursor = mydb.cursor()

sql = "select id, profile_link, nickname, hours_played_limit from users"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(myresult)
mydb.commit()
# MySQL select Stop

for profile_link in myresult:

    # MySQL select Start
    mycursor = mydb.cursor()
    sql = "select sum(time_played) from user_steam_games where user_id =" + str(profile_link[0])
    mycursor.execute(sql)
    time_played_old = mycursor.fetchone()
    print(time_played_old)
    # MySQL select Stop

    # URL PART Start
    URL = 'https://steamcommunity.com/id/' + profile_link[1] + '/games/?tab=all'
    page = requests.get(URL)
    data = BeautifulSoup(page.content, 'html.parser')
    results = data.find('script', language='javascript')
    txt = str(results)
    x = txt.split('"')
    # URL PART End

    # URL PART Start 2 - Steam has 2 links for user profiles.
    # One for custom names like "piotref1" and other with string of numbers as id
    if x[0] == 'None':
        # URL PART Start
        URL = 'https://steamcommunity.com/profiles/' + profile_link[1] + '/games/?tab=all'
        page = requests.get(URL)
        data = BeautifulSoup(page.content, 'html.parser')
        results = data.find('script', language='javascript')
        txt = str(results)
        x = txt.split('"')
        # URL PART End
    # URL PART End 2 - Steam has 2 links for user profiles.

    # Data values to find definition START
    search_attribute = ['appid', 'name', 'hours_forever', 'achievements'] # Declaring what we want to find in the website data we loaded in
    matched_indexes_appid = []
    matched_indexes_name = []
    matched_indexes_playtime = []
    matched_indexes_achievements = []
    # Data values to find definition STOP

    i = 0
    length = len(x)

    # Loop for comparing data in scraped data for matches declared in search_attribute Start
    while i < length:
        if search_attribute[0] == x[i]:
            matched_indexes_appid.append(i + 1)
        if search_attribute[1] == x[i]:
            matched_indexes_name.append(i + 2)
        if search_attribute[2] == x[i]:
            matched_indexes_playtime.append(i + 2)
        if search_attribute[3] == x[i]:
            matched_indexes_achievements.append(i + 1)
        i += 1
    # Loop for comparing data in scraped data for matches declared in search_attribute Start

    length_playtime = len(matched_indexes_playtime)
    length_name = len(matched_indexes_name)
    i = 0

    while i < length_name:
        tmp_txt0 = x[matched_indexes_appid[i]]
        tmp_txt0 = tmp_txt0.replace(":", "")
        tmp_txt0 = tmp_txt0.replace(",", "")

        tmp_txt1 = x[matched_indexes_name[i]]

        # Filling out empty space in playtime compared to amount of games START
        if i > length_playtime:
            tmp_txt2 = '0'
        elif i < length_playtime:
            tmp_txt2 = x[matched_indexes_playtime[i]]
        # Filling out empty space in playtime compared to amount of games STOP

        tmp_txt3 = x[matched_indexes_achievements[i]]
        tmp_txt3 = tmp_txt3.replace(":", "")
        tmp_txt3 = tmp_txt3.replace(",", "")

        # MySQL insert steam_games Start
        mycursor = mydb.cursor()
        # Changing String to boolean (0,1) START
        if(tmp_txt3 == "false"):
            tmp_txt3 = 0
        elif tmp_txt3 == "true":
            tmp_txt3 = 1
        # Changing String to boolean (0,1) STOP

        sql = "INSERT INTO steam_games(appid,title,has_achievements) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE title= values(title), has_achievements = values(has_achievements)"
        mycursor.execute(sql, (int(tmp_txt0), str(tmp_txt1), str(tmp_txt3)))
        mydb.commit()
        # MySQL insert steam_games Stop

        # MySQL insert steam_user_games Start
        mycursor = mydb.cursor()
        tmp_txt2 = tmp_txt2.replace(',', '')
        id = str(profile_link[2]) + '#' + str(tmp_txt0)

        sql = "INSERT INTO user_steam_games(id,user_id,game_id,time_played) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE time_played= values(time_played)"
        mycursor.execute(sql, (str(id), int(profile_link[0]), str(tmp_txt0), str(tmp_txt2)))
       # print(profile_link[0])
       # print(tmp_txt0)
        mydb.commit()
        # MySQL insert steam_games Stop

        i += 1

    # MySQL select Start
    mycursor = mydb.cursor()
    sql = "select sum(time_played) from user_steam_games where user_id =" + str(profile_link[0])
    mycursor.execute(sql)
    time_played_new = mycursor.fetchone()
    # MySQL select Stop

    # Automated sending Email if played hours are above limit START
    if time_played_old[0] is not None:
        time_played_difference = time_played_new[0] - time_played_old[0]
        if (time_played_difference > profile_link[3]) and (profile_link[3] > 0):
            test_parent(profile_link[0], time_played_difference)
    # Automated sending Email if played hours are above limit START
