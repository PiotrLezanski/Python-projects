import smtplib


def send_email(email, height, average_height, count):
    from_email = "testudemystudent@gmail.com"
    from_password = "pythonlecture"
    to_email = email

    subject = "Height data"
    message = "Hey! Your height is %s. The average of all data is %s and that is " \
              "calculated out od %s of people" % (height, average_height, count)

    email_text = """
    From: %s
    To: %s
    Subject: %s
    
    %s
    """ % (from_email, to_email, subject, message)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, email_text)
        server.close()

        print("Email sent!")
    except:
        print("something went wrong")
