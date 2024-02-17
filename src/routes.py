from flask import render_template, request, redirect, url_for, flash, session
from models import User
from database import session
from app import app
# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Registration page route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if email already exists in the database
        if session.query(User).filter_by(email=email).first():
            flash('Email already exists. Please choose a different email.', 'danger')
            return redirect(url_for('register'))

        # Create a new user object and add it to the database
        new_user = User(username=username, email=email, password=password)
        session.add(new_user)
        session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Login page route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Retrieve user by email
        user = session.query(User).filter_by(email=email).first()

        # Check if user exists and password is correct
        if user and user.password == password:
            # Store user ID in session to indicate user is logged in
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('mentorship_dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

# Mentorship dashboard route (requires authentication)
@app.route('/dashboard')
def mentorship_dashboard():
    # Check if user is logged in
    if 'user_id' in session:
        return render_template('mentorship_dashboard.html')
    else:
        flash('You need to login first.', 'danger')
        return redirect(url_for('login'))

# Logout route
@app.route('/logout')
def logout():
    # Logout user
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))
