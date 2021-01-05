from flask import Blueprint, render_template,request ,redirect,session,url_for
# from blog.db import get_db
import sqlite3
from datetime import datetime
# from blog.__init__ import task_list,tasks_list,tasks,index_lists



home_bp = Blueprint('home', __name__)


# index variable for tasks list
index_lists = 1
# index variable for tasks
index_tasks = 1
# index variable for remove and edit list
index = 1

# lists variable
task_list = {}
tasks_list = {}
task_list['tasks'] = []

# tasks variable
task = {}
tasks = {}

@ home_bp.route('/home')
def home():
    return render_template('page/home.html', tasks_list=tasks_list, tasks=tasks)


# login templates
@home_bp.route('/')
def login():
    if request.method == 'GET':
        return render_template('login/login.html')
    else:
        #read values from form
        login = request.form['login']
        password = request.form['password']
        print(password,login)
        print('hello')
        if login == 'malak' and password == 'mm1234':
        
            #redirect to home
            return redirect(url_for('home'))

        else:
            return render_template('login/login.html')
