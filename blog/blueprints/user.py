import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for
from blog.db import get_db

# define our blueprint
user_bp = Blueprint('user', __name__)


@user_bp.route('/add/user', methods=['GET', 'POST'])
def add_user():
    
    if request.method == 'GET':
        # render add user blueprint
        return render_template('user/index.html')
    else:
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']

        # get the DB connection
        db = get_db()

        # insert user into DB
        try:
            # execute our insert SQL statement
            db.execute("INSERT INTO user (username, password, firstname, lastname) VALUES (?, ?, ?, ?);", (username, password, first_name,last_name))

            # write changes to DB
            db.commit()
            
            return redirect(url_for('/home'))


        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")

@user_bp.route('/users')
def get_users():
    # get the DB connection
    db = get_db()

    # get all users from the db
    users = db.execute('select * from user').fetchall()

    # render 'list.html' blueprint with users
    return render_template('user/list.html', users=users)
