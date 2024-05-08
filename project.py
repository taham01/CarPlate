from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page1.html')

@app.route('/search', methods=['POST'])
def search():
    plate_number = request.form['plate_number']

    db_connection = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        password = '2549FDFAb@',
        database = "carDataBase"
    )


    """plate_number = input("Enter the plate number of the car: ")"""

    cursor = db_connection.cursor()

    query = "SELECT OwnerPhoneNumber, OwnerName, CarMake FROM Cars WHERE PlateNumber = %s"
    cursor.execute(query, (plate_number,))

    result = cursor.fetchone()

    cursor.close()
    db_connection.close()

    if result:
        owner_phone_number, owner_name, car_make = result
        """"print(f"Plate Number: {plate_number}")
        print(f"Owner's Phone Number: {owner_phone_number}")
        print(f"Owner's Name: {owner_name}")
        print(f"Car Make: {car_make}")"""

        return render_template('page2.html', plate_number=plate_number, owner_phone_number=owner_phone_number, owner_name=owner_name, car_make=car_make)
    else:
        """print("Car not found in the database")"""
        return "Car not found in the database"

if __name__ == '__main__':
    app.run(debug=True)
