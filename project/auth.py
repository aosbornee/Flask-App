from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required
from datetime import datetime as dt


# TODO: Add Functionality to the quiz.html page using forms and inputs,
#  these can then be checked against a txt or some file that stores the answers
# DONE

# TODO: Create a forbidden site that users cannot enter, this page will have a list of all users

# TODO: Add a Column to my User Table which stores what time the user created their account
# DONE

# TODO: Change the current stylesheet that I am using, implement my own JS and CSS

# TODO: Create a medium, then hard difficulty quiz (this would ask for user to write code)

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    # here we are doing a query that looks for the email in the db that was inputted by the user
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        if 'counter' not in session:
            session['counter'] = 0
            # using sessions to prevent max number of password attempts
        session['counter'] = session.get('counter') + 1
        if session.get('counter') == 2:
            flash('You have one attempt remaining..')
        if session.get('counter') == 3:
            flash('You have exceeded maximum no of tries')
            session.pop('counter', None)
            return render_template('404.html')
        # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page
    else:
        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    if len(password) < 5 or len(password) > 20:
        flash("Password must be within 5-30 characters")
        return redirect(url_for('auth.signup'))

    user = User.query.filter_by(email=email).first() # If this returns a user, then the email is already in our database

    if user:
    # if not user or not check_password_hash(user.password, password):

        flash('This email address already exists, Please Login')
        return redirect(url_for('auth.login'))

    # Here we are creating a new user, their password is then hashed and stored in the db
    else:
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), created=dt.now())

    # here we are then adding that user to the database, so when they next come to login we have their details stored
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/view')
def view():
    # Here we are creating a template that will list all of the users on our website
    # This is done by running a query to our db
    return render_template('view.html', values=User.query.all())


@auth.route('/404')
def page_not_found():
    return render_template('404.html')