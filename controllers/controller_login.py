from flask import render_template, request, redirect, url_for, session
import json
import os


def login():
    # If the request method is GET, display the login form
    if request.method == 'GET':
        return render_template('login.html')
    current_path = os.getcwd()
    print("Current Path:", current_path)

    # Get the entered username and password from the form
    username = request.form['username']
    password = request.form['password']
    try:
        with open('./data/users.json', 'r') as f:
            users = json.load(f)
            for user in users:
                if user['username'] == username and user['password'] == password:
                    # If it exists, store the username in the session and redirect the user to the dashboard
                    session['username'] = username
                    session['visits'] = user['visits']
                    return redirect(url_for('dashboard'))

    except Exception as e:
        return render_template('login.html', error=e)

    error = "Invalid username or password. Please try again."
    return render_template('login.html', error=error)
    # Check if the username and password combination exists in the dictionary


