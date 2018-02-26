import csv
import random
import datetime
from datetime import timedelta

from sqlAPI import getTables, clearTable

# number of records needed names needed
num_of_records = 100
name_length = 34
list_of_tables = []


class Booking:
    def __init__(self, db, table_name='booking'):
        cursor = db.cursor()
        list_of_tables = getTables(cursor)
        clearTable(cursor, 'booking', 'serial_no')
        db.commit()

        # Read from CSV
        csvReadaer_fn = csv.reader(open('first_name.csv', newline=''), delimiter=' ', quotechar='|')
        csvReadaer_ln = csv.reader(open('first_name.csv', newline=''), delimiter=' ', quotechar='|')
        first_name_list = [row for row in csvReadaer_fn]
        last_name_list = [row for row in csvReadaer_ln]

        first_name_list_len = len(first_name_list)
        last_name_list_len = len(last_name_list)

        email_ending = ["@gmail.com","@mail.mcgill.ca", "@mcgill.com", "@outlook.com", "@spinbiek.com"]
        email_ending_len = len(email_ending)

        for i in range(num_of_records):

            cursor.execute("select user_email from spin_bike_users;")
            user_email = cursor.fetchall()[random.randrange(100)][0]

            # Random time
            booking_time = datetime.datetime(2018, 1, 1, 0, 0, 0) + \
                         timedelta(days=random.randrange(30)) + \
                         timedelta(hours=random.randrange(24)) + \
                         timedelta(minutes=random.randrange(60)) + \
                         timedelta(seconds=random.randrange(60))

            cursor.execute("""INSERT INTO booking (booking_time , user_email , serial_no) VALUES (%(b_id)s, %(email)s, %(s_no)s);""" ,
                           {'b_id': booking_time,
                            'email': user_email,
                            's_no': random.randint(101,130)})

            db.commit()
