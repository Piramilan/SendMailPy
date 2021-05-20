 ##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

my_email = "MilanPython98@Gmail.Com"
password = "Python98Milan"

data = pandas.read_csv('birthdays.csv')
birthday_dict = {(data_row['month'],data_row['day']):data_row for (index,data_row) in data.iterrows()}

today = (dt.datetime.now().month,dt.datetime.now().day)

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contects = letter_file.read()
        contects = contects.replace('[NAME]',birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email
                            , to_addrs=birthday_person['email']
                            , msg=f"Subject:Hello Milan\n\n{contects}"
                            )
