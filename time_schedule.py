import csv
import random
import datetime
from datetime import timedelta


# number of records needed names needed
num_of_records = 100
name_length = 34
list_of_tables = []


class TimeSchedule:
    def __init__(self, db, table_name='booking'):
        cursor = db.cursor()
        db.commit()



        cursor.execute("select bmemail from caretaker;")
        caretakers = cursor.fetchall()


        cursor.execute("select place_id from places;")
        places = cursor.fetchall()
        places_length = len(places)

        schedule_day = ['M', 'T', 'TR', 'F', 'S', 'WF']

        for caretaker in caretakers:

            bmemail = caretaker[0]
            place_id = places[random.randrange(places_length)][0]
            day = schedule_day[random.randrange(6)]
            schedule_time = datetime.datetime(2018, 1, 1, 0, 0, 0) + \
                         timedelta(hours=random.randrange(23)) + \
                         timedelta(minutes=random.randrange(59)) + \
                         timedelta(seconds=random.randrange(59))


            print(bmemail, place_id, day, schedule_time.time())


            cursor.execute("""INSERT INTO time_schedule  VALUES (%(bmemail)s, %(place_id)s, %(day)s, %(schedule_time)s);""" ,
                           {'bmemail': bmemail,
                            'place_id': place_id,
                            'day': day,
                            'schedule_time': schedule_time})

            db.commit()

        # # Random time
        # maintenance_date = datetime.datetime(2018, 1, 1, 0, 0, 0) + \
        #              timedelta(days=random.randrange(30)) + \
        #              timedelta(hours=random.randrange(24)) + \
        #              timedelta(minutes=random.randrange(60)) + \
        #              timedelta(seconds=random.randrange(60))
        #
        # maintenance_date | bmemail | place_id | are_plants_watered | is_area_clean | does_computer_work | additional_comments
        #
        # cursor.execute("""INSERT INTO booking (booking_time , user_email , serial_no) VALUES (%(b_id)s, %(email)s, %(s_no)s);""" ,
        #                {'b_id': booking_time,
        #                 'email': user_email,
        #                 's_no': random.randint(101,130)})
        #
        # db.commit()
