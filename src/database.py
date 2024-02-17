import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace 'sqlite:///data/mentorship.db' with your actual database URI
engine = create_engine('sqlite:////Users/mac/IdeaProjects/Google/data/mentorship.db')
Session = sessionmaker(bind=engine)
session = Session()


# Function to establish database connection
def get_db_connection():
    conn = sqlite3.connect('data/mentorship.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to insert a new user into the database
def insert_user(username, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()

# Function to retrieve user by email
def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

# Function to check if email already exists in the database
def email_exists(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE email=?", (email,))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0