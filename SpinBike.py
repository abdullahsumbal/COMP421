import datetime
from datetime import timedelta
import random
from sqlAPI import getTables, clearTable

class spinBike:
    def __init__(self, db, table_name='spinbike'):
        self.db = db
        self.cursor = db.cursor()
        self.serial_no = 100
        self.spin_bike_data = {}
        number_of_record = 30
        list_of_tables = getTables(self.cursor)
        clearTable(self.cursor, "spin_bike_usage", 'serial_no')
        clearTable(self.cursor, table_name, 'serial_no')
        db.commit()
        for i in range(number_of_record):
            self.populateData()

    def populateData(self):

        # Model
        models = ['Life Fitness IC5', 'Keiser M3i ', 'Keiser M3i-HV', 'LeMond RevMaster', 'Fit Spin Pro']
        brand_model = models[random.randint(0, len(models)-1)]

        #serial_no | brand_model | last_battery_charge_time | has_datacollector

        self.serial_no += 1
        last_batter_change_time = datetime.datetime(2018, 1, 1, 3) +\
                                  timedelta(days=random.randrange(30)) +\
                                  timedelta(minutes=random.randrange(60)) +\
                                  timedelta(hours= random.randrange(12))

        has_datacollector = "yes" if random.randrange(2) == 1 else "No"

        self.cursor.execute("""
             INSERT INTO spinbike (serial_no, brand_model, last_battery_charge_time, has_datacollector)
             VALUES (%(str1)s, %(str2)s, %(date)s, %(str3)s);
             """,{'str1': self.serial_no, 'str2': brand_model, 'date': last_batter_change_time, 'str3': has_datacollector})
        self.spin_bike_data[self.serial_no] = [brand_model, last_batter_change_time, has_datacollector]

        self.db.commit()









