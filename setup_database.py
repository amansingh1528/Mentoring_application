import sqlite3
import os

# Function to create the database and table
def create_database():
    conn = sqlite3.connect('data/mentorship.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                    )''')

    conn.commit()
    conn.close()

# Function to insert sample data into the database
def insert_sample_data():
    conn = sqlite3.connect('data/mentorship.db')
    cursor = conn.cursor()

    # Sample user data
    sample_users = [
        ("Alice", "alice@example.com", "password1"),
        ("Bob", "bob@example.com", "password2"),
        ("Charlie", "charlie@example.com", "password3"),
        ("David", "david@example.com", "password4"),
        ("Eve", "eve@example.com", "password5"),
        ("Frank", "frank@example.com", "password6"),
        ("Grace", "grace@example.com", "password7"),
        ("Hannah", "hannah@example.com", "password8"),
        ("Isaac", "isaac@example.com", "password9")
    ]

    # Insert sample data into the users table
    cursor.executemany("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", sample_users)

    conn.commit()
    conn.close()

# Create database and insert sample data
if __name__ == "__main__":
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    create_database()
    insert_sample_data()
    print("Sample data inserted successfully.")
