import csv
import random
import datetime
from datetime import timedelta


# number of records needed names needed
num_of_records = 100
name_length = 34
list_of_tables = []


class Maintenance:
    def __init__(self, db, table_name='booking'):
        cursor = db.cursor()
        db.commit()

        cursor.execute("select bmemail ,place_id  from time_schedule;")
        schedule = cursor.fetchall()
        schedule_length = len(schedule)
        does_computer_work = ['Yes', 'No']
        is_area_clean = ['Yes', 'No', 'Very Dirty', 'super clean']
        are_plants_watered= ['Yes', 'No']
        additional_comments = 'None'

        for i in range(num_of_records):


            #maintenance_date | bmemail | place_id | are_plants_watered | is_area_clean | does_computer_work | additional_comments

            # Random time
            maintenance_date = datetime.datetime(2018, 1, 1, 0, 0, 0) + \
                         timedelta(days=random.randrange(30)) + \
                         timedelta(hours=random.randrange(24)) + \
                         timedelta(minutes=random.randrange(60)) + \
                         timedelta(seconds=random.randrange(60))

            index = random.randrange(schedule_length)
            bmemail = schedule[index][0]
            place_id = schedule[index][1]

            cursor.execute("""INSERT INTO maintenance (maintenance_date, bmemail, place_id, are_plants_watered, is_area_clean, does_computer_work, additional_comments) VALUES (%(maintenance_date)s, %(bmemail)s, %(place_id)s, %(are_plants_watered)s, %(is_area_clean)s, %(does_computer_work)s, %(additional_comments)s);""" ,
                           {'maintenance_date': maintenance_date,
                            'bmemail': bmemail,
                            'place_id': place_id,
                            'are_plants_watered': are_plants_watered[random.randrange(2)],
                            'is_area_clean': is_area_clean[random.randrange(4)],
                            'does_computer_work': does_computer_work[random.randrange(2)],
                            'additional_comments': additional_comments})
            db.commit()
