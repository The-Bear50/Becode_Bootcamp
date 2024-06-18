import datetime
from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
import bleach

app = Flask(__name__)


def connect_db(self):
    # MySQL CONNECT
    config = {
        'user': 'root',
        'password': '',
        'database': 'messages',
        'host': 'localhost:3306',
        'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
        'raise_on_warnings': True
    }

    try:
        cnx = mysql.connector.connect(**config)
        # cursor = cnx.cursor(dictionary=True)

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection and cursor
        if cnx.is_connected():
            # cursor.close()
            # cnx.close()
            print("MySQL connection is closed.")

        return cnx


@app.route("/", methods=['GET', 'POST'])

def contact():
    config = {
        'user': 'root',
        'password': '',
        'database': 'messages',
        'host': 'localhost',
        'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
        'raise_on_warnings': True
    }
    cnx = mysql.connector.connect(**config)


    if request.method == 'POST':
        # Getting data from the form
        name = bleach.clean(request.form.get('name'))
        email = bleach.clean(request.form.get('email'))
        subject = bleach.clean(request.form.get('subject'))
        message = bleach.clean(request.form.get('message'))
        date = bleach.clean(str(datetime.datetime.now()))

        # Insert the data into the database
        if cnx:
            try:
                cursor = cnx.cursor()
                query = ("INSERT INTO messages (name, email, subject, message, date) "
                         "VALUES (%s, %s, %s, %s, %s)")
                cursor.execute(query, (name, email, subject, message, date))
                cnx.commit()
                cursor.close()
                cnx.close()
                return "Message submitted successfully"
            except Error as e:
                print(f"Error: {e}")
                return "Failed to submit message"
        else:
            return "Failed to connect to the database"

    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
       # db.create_all()  # Create tables if they don't exist
        app.run(debug=True)