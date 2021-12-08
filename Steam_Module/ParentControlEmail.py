# MySQL connection Start

from Database import db_con

mydb = db_con()
mycursor = mydb.cursor()

# MySQL connection Stop


def test_parent(id, time_played_difference):
    # MySQL insert Start
    mycursor = mydb.cursor()

    sql = "select email from users where id=" + str(id)
    mycursor.execute(sql)
    email = mycursor.fetchone()
    print(time_played_difference)

    mydb.commit()
    # MySQL insert Stop

    import smtplib
    print(email)
    gmail_user = 'sdas'
    gmail_password = 'csadas'

    sent_from = gmail_user
    to = email[0]
    subject = 'Parent alert!'
    body = 'Your child has played for ' + str(time_played_difference) + 'hours today. In case the time exceeds 24hrs ' \
                                                                        'or time between the wake up time and sleep ' \
                                                                        'time of child there are few options: ' \
                                                                        'Option 1: Games running in background and computer being left on during the night. Common with idle games.' \
                                                                        'Option 2: Multiple games running at same time. Please check account for idle game time and other g ame that was played recently.'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, to, subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        print("test 1")
        smtp_server.ehlo()
        print("test 2")
        smtp_server.login(gmail_user, gmail_password)
        print("test 3")
        smtp_server.sendmail(sent_from, subject, to, email_text)
        print("test 4")
        smtp_server.close()
        print("test 5")
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)