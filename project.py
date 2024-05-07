import mysql.connector
db_connection = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = 'Elio-2022',
    database = "carDataBase"
)


plate_number = input("Enter the plate number of the car: ")

cursor = db_connection.cursor()

query = "SELECT OwnerPhoneNumber, OwnerName, CarMake FROM Cars WHERE PlateNumber = %s"
cursor.execute(query, (plate_number,))

result = cursor.fetchone()

if result:
    owner_phone_number, owner_name, car_make = result
    print(f"Plate Number: {plate_number}")
    print(f"Owner's Phone Number: {owner_phone_number}")
    print(f"Owner's Name: {owner_name}")
    print(f"Car Make: {car_make}")
else:
    print("Car not found in the database")

cursor.close()
db_connection.close()