# Project: Form in Python with Flask

### Skills worked

 - Backend: PYTHON programming (introduction to logical structures)
 - Sanitization and validation of a form
 - Implementing POST and GET methods
 - Implementing templates with Jinja

# Walkthrough

## Setup
- Python 3.x
- MySQL server or MongoDB server
- The following Python packages:
  - Flask
  - Flask-SQLAlchemy (for MySQL)
  - mysql-connector-python (for MySQL)
  - Flask-PyMongo (for MongoDB)
  - bleach

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/The-Bear50/Becode_Bootcamp.git
cd Scripting/Python/Flask form
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate
```

3. **Install the dependencies:**

```bash
pip install Flask Flask-SQLAlchemy mysql-connector-python Flask-PyMongo bleach
```
### MySQL Setup

1. **Set up the MySQL database:**

- Ensure your MySQL server is running (through [XAAMP](https://www.apachefriends.org/index.html), for example)

2. **Create a database named messages and a table named messages with the following schema:**

```sql

CREATE DATABASE messages;
USE messages;

CREATE TABLE messages (
    sno INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(35) NOT NULL,
    subject VARCHAR(50) NOT NULL,
    message VARCHAR(120) NOT NULL,
    date VARCHAR(12) DEFAULT NULL
);
```

3. **Update the database configuration:**
- Open flask_app.py and update the database configuration in the get_db_connection function with your MySQL username, password, host, and other details.

### MongoDB Setup

1. Set up the MongoDB database:

- Ensure your MongoDB server is running.

2. Configure MongoDB in the Flask app:

- Update the MONGO_URI in flask_app.py to match your MongoDB connection string.

## Usage

1. **Run the Flask application:**

```bash
python flask_app.py
```

2. **Access the application:**

- Open your web browser and navigate to http://127.0.0.1:5000/.
- Fill out the contact form and submit it.

![image-1](https://github.com/The-Bear50/Becode_Bootcamp/assets/85135970/534593e2-6dba-4702-b959-ccf70195305b)

![image-2](https://github.com/The-Bear50/Becode_Bootcamp/assets/85135970/100f58e5-1666-4509-8756-0d2263ff27e9)

3. **Database Connection:**
- MySQL:
  - The application connects to the MySQL database using the mysql.connector library.
  - Form submissions are inserted into the messages table in the messages database.

![image-3](https://github.com/The-Bear50/Becode_Bootcamp/assets/85135970/c99db656-198d-4d9d-a9bb-d3359bbd40ba)

![image-4](https://github.com/The-Bear50/Becode_Bootcamp/assets/85135970/93640635-cc90-4f48-9494-0c78e051a089)

- MongoDB:
  - The application connects to the MongoDB database using the Flask-PyMongo library.
  - Form submissions are inserted into the 'messages' collection in the 'messages' database.

![image](https://github.com/The-Bear50/Becode_Bootcamp/assets/85135970/fcbf7aa8-8902-444a-8a6c-208b13041b7c)


## Project Structure

```arduino

flask-contact-form/
│
├── flask_app.py
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        ├── jquery.min.js
        ├── popper.js
        ├── bootstrap.min.js
        ├── jquery.validate.min.js
        └── main.js
