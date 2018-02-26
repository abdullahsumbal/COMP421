import random
from sqlAPI import getTables, clearTable

class places:
    def __init__(self, db, table_name='places'):
        self.db = db
        self.cursor = db.cursor()
        self.place_id = 0
        number_of_record = 50
        clearTable(self.cursor, table_name, 'place_id')
        db.commit()
        for i in range(number_of_record):
            self.populateData()

    def populateData(self):

        # Model
        addresses = ['Trottier building', 'McLennan Library', 'Redpath Library', 'Old Music Building', 'New Music Building', 'New Residence', 'Arts Building', 'Schulich Library', 'Wirth Music Building', 'Stewart Biology Building']
        address = addresses[random.randrange(len(addresses))]
        room_number = random.choice([random.randint(100,105),random.randint(210,220),random.randint(300,305)])


        self.place_id += 1
        self.cursor.execute("""
             INSERT INTO places (place_id, address, room_number)
             VALUES (%(id)s, %(address)s, %(room)s);
             """,{'id': self.place_id, 'address': address, 'room': room_number})

        self.db.commit()








