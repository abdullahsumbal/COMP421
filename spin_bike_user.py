import csv
import random
from sqlAPI import getTables, clearTable

# number of records needed names needed
num_of_records = 100
name_length = 34
list_of_tables = []


class SpinBikeUser:
    def __init__(self, db, table_name='Spin_Bike_Users'):
        cursor = db.cursor()
        list_of_tables = getTables(cursor)
        clearTable(cursor, 'spin_bike_users', 'user_email')
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

            # randomly select the name and email
            first_name = ''
            last_name = ''
            length_check = False
            while (not length_check):
                first_name = ''.join(first_name_list[random.randrange(first_name_list_len)])
                last_name = ''.join(last_name_list[random.randrange(last_name_list_len)])
                # length check
                if len(first_name + last_name) < name_length:
                    length_check = True
            # Full name
            user_name = first_name + ' '  + last_name
            user_email = first_name + '.' + last_name + email_ending[random.randrange(email_ending_len)]

            cursor.execute("""INSERT INTO spin_bike_users (user_email, user_name) VALUES (%s, %s);""" ,
                           (user_email,
                            user_name))

        db.commit()
