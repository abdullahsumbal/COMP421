import psycopg2
from spin_bike_user import SpinBikeUser
from BikeManager import bikeManager
from SpinBike import spinBike

def init_connection():
    db = psycopg2.connect(host="comp421.cs.mcgill.ca", database="xx", user="xx", password="xx")

    #SpinBikeUser(db)
    #bikeManager(db)
    spinBike(db)


    db.close()


if __name__ == '__main__':
    init_connection()
