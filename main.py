import psycopg2
from spin_bike_user import SpinBikeUser
from BikeManager import bikeManager
from SpinBike import spinBike
from SpinBikeUsage import spinBikeUsage
from Places import places
from booking import Booking

def init_connection():
    db = psycopg2.connect(host="comp421.cs.mcgill.ca", database="xxxx", user="xxxxx", password="xxxx")

    # SpinBikeUser(db)
    # bikeManager(db)
    # spin_bike = spinBike(db)
    # spinBikeUsage(db, spin_bike.spin_bike_data)
    places(db)
    # Booking(db)



    db.close()


if __name__ == '__main__':
    init_connection()
