import datetime
from datetime import timedelta
import random
from sqlAPI import getTables, clearTable

class spinBikeUsage:
    def __init__(self,db, spin_bike_data, table_name="spin_bike_usage"):
        self.db = db
        self.cursor = db.cursor()
        self.spin_bike_data = spin_bike_data
        clearTable(self.cursor, table_name, 'serial_no')
        number_of_record = 200
        self.db.commit

        self.serial_no_list= []
        self.serial_no_list_len = 0

        # find the serial number
        for k,v in self.spin_bike_data.items():
            if v[2]=="yes":
                self.serial_no_list.append(k)
                self.serial_no_list_len +=1

        for i in range(200):
            self.populate_data()


    def populate_data(self):

        # Random time
        start_time = datetime.datetime(2018, 1, 1, 0,0,0 ) +\
                     timedelta(days= random.randrange(30)) +\
                     timedelta(hours=random.randrange(24)) +\
                     timedelta(minutes=random.randrange(60)) +\
                     timedelta(seconds=random.randrange(60))

        # Random duration
        duration = random.randrange(60)

        # Random serial number
        serial_no= self.serial_no_list[random.randrange(self.serial_no_list_len)]
        self.cursor.execute("""
             INSERT INTO spin_bike_usage (start_time, serial_no, duration)
             VALUES (%(date)s, %(int)s, %(int1)s);
             """,{'date': start_time, 'int': serial_no, 'int1': duration,})

        self.db.commit()
