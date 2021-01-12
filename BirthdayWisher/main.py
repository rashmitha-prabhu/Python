import os
import pandas
import smtplib
import random
import datetime as dt

data = pandas.read_csv('birthdays.csv', index_col=0).to_records()

my_email = "samplemail@gmail.com"
password = "password"

now = dt.datetime.today()

for row in data:
    date = dt.datetime(year=now.year, month=row['month'], day=row['day'])
    if now.month == date.month and now.day == date.day:
        file = random.choice(os.listdir('letter_templates'))
        with open(f'letter_templates/{file}') as data:
            letter = data.read()
            letter = letter.replace("[NAME]", row['name'])

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(my_email, password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=row['email'],
                    msg=f"Subject: It's your birthday!\n\n"
                        f"{letter}"
                )
