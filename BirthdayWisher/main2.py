import smtplib
import datetime as dt
import random

my_email = "rashmithaprabhu920@gmail.com"
password = 'abc123()'

now = dt.datetime.today()
day = now.weekday()

if day == 0:
    with open("quotes.txt") as data:
        quotes = data.readlines()
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rashmitha.prabhu920@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{random.choice(quotes)}".encode("utf-8")
        )
