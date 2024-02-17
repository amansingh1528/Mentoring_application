from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
def get_db_connection():
    conn = sqlite3.connect('data/mentorship.db')
    conn.row_factory = sqlite3.Row
    return conn

# Database operation to insert a new user into the database
def insert_user(username, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()

# Database operation to check if a user with the given email already exists
def is_valid_user(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Authentication function to check if the user is logged in
def user_authenticated():
    return session.get('logged_in')

# Logout function to clear session data
def logout_user():
    session.clear()

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Save user data to the database
        insert_user(username, email, password)
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Check user credentials
        if is_valid_user(email, password):
            session['logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('mentorship_dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

# Mentorship dashboard (requires authentication)
@app.route('/dashboard')
def mentorship_dashboard():
    # Check if user is authenticated
    if user_authenticated():
        return render_template('mentorship_dashboard.html')
    else:
        flash('You need to login first.', 'danger')
        return redirect(url_for('login'))

# Logout
@app.route('/logout')
def logout():
    # Logout user
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
