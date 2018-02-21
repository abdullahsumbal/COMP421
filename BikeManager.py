import csv
import random
import string
from sqlAPI import getTables, clearTable

# number of records needed names needed
num_of_records = 100
name_length = 19
password_min_length = 6
password_max_length = 12

class bikeManager:

    # Random password generator
    def randompassword(self):
      chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
      size = random.randint(password_min_length, password_max_length)
      return ''.join(random.choice(chars) for x in range(size))

    def __init__(self, db, table_name='bikemanagers'):
        cursor = db.cursor()
        list_of_tables = getTables(cursor)
        clearTable(cursor, 'administrator', 'bmemail')
        clearTable(cursor, 'caretaker', 'bmemail')
        clearTable(cursor, table_name, 'bmemail')

        # Read from CSv
        csvReadaer_fn = csv.reader(open('first_name.csv', newline=''), delimiter=' ', quotechar='|')
        csvReadaer_ln = csv.reader(open('first_name.csv', newline=''), delimiter=' ', quotechar='|')
        first_name_list = [row for row in csvReadaer_fn]
        last_name_list = [row for row in csvReadaer_ln]

        first_name_list_len = len(first_name_list)
        last_name_list_len = len(last_name_list)

        email_ending = ["@gmail.com", "@mail.mcgill.ca", "@mcgill.com", "@outlook.com", "@spinbiek.com"]
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
            bmname = first_name + ' ' + last_name
            bmemail = first_name + '.' + last_name + email_ending[random.randrange(email_ending_len)]
            bmpassword = self.randompassword()
            #print((bmname), (bmemail))

            cursor.execute("""INSERT INTO bikemanagers (bmemail , bmname , bmpassword) VALUES (%s, %s, %s);""",
                           (bmemail,
                            bmname,
                            bmpassword))
            db.commit()
            select_role = random.randrange(10)
            if 0 <= select_role <= 2:
                cursor.execute("""INSERT INTO administrator (bmemail) VALUES (%s);""",
                               (bmemail,))
            if 3 <= select_role <= 7:
                cursor.execute("""INSERT INTO caretaker (bmemail) VALUES (%s);""",
                               (bmemail,))
            db.commit()






# # Connection to the database
# db = psycopg2.connect(host="comp421.cs.mcgill.ca",database="cs421", user="cs421g29", password="spinBike4!")
#
# # Prepare a cursor object using cursor() method
# cursor = db.cursor()
#


#
#
# # disconnect from server
# db.close()