from flask import render_template, session, url_for, redirect
from week9.utils.utils import update_user_in_file


def dashboard():
    # Check if the user is authenticated
    if 'username' in session:
        update_user_in_file(session['username'])
        return render_template('dashboard.html')
    else:
        # If the user is not authenticated, redirect to the login page
        return redirect(url_for('login'))
