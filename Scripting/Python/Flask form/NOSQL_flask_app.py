import datetime
from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
import bleach
from flask_pymongo import PyMongo

app = Flask(__name__)


# Configure MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/messages"
mongo = PyMongo(app)

@app.route("/", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Getting data from the form
        name = bleach.clean(request.form.get('name'))
        email = bleach.clean(request.form.get('email'))
        subject = bleach.clean(request.form.get('subject'))
        message = bleach.clean(request.form.get('message'))
        date = datetime.datetime.now()

        # Insert the data into MongoDB
        try:
            mongo.db.messages.insert_one({
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
                'date': date
            })
            return "Message submitted successfully"
        except Exception as e:
            print(f"Error: {e}")
            return "Failed to submit message"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)