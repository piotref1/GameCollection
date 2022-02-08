# MySQL connection Start
from Database import db_con
import smtplib
mydb = db_con()
mycursor = mydb.cursor()
# MySQL connection Stop


def email_parent(id, time_played_difference):
    # MySQL insert Start
    mycursor = mydb.cursor()

    sql = "select email from users where id=" + str(id)
    mycursor.execute(sql)
    email = mycursor.fetchone()
    print(time_played_difference)

    mydb.commit()
    # MySQL insert Stop

    print(email)
    gmail_user = 'text'
    gmail_password = 'text'

    sent_from = gmail_user
    to = email[0]
    subject = 'Parent alert!'
    body = "Your child has played for " +\
           str(time_played_difference) + "hours today. In case the time exceeds 24hrs or time" +\
           " between the wake up time and sleep time of child please check computer."
    subject = "Game Library Parent Alarm"
    message = 'Subject: {}\n\n{}'.format(subject, body)
    # Create your SMTP session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # Use TLS to add security
    smtp.starttls()

    # User Authentication
    smtp.login(gmail_user, gmail_password)

    try:
        # Sending the Email
        smtp.sendmail(sent_from, email[0], message)

        # Terminating the session
        smtp.quit()
        print("Email sent successfully!")

    except Exception as ex:
        print("Something went wrong....", ex)