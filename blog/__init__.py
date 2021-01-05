from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from .blueprints.lists import lists_bp
from .blueprints.home import home_bp
from .blueprints.tasks import tasks_bp

import os

from flask import Flask


def create_app(test_config=None):
    # create the Flask
    app = Flask(__name__, instance_relative_config=True)

    # configure the app
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import helper DB functions
    from . import db
    db.init_app(app)

    # register the 'list' blueprint
    from .blueprints.lists import lists_bp
    app.register_blueprint(lists_bp)
    
    from .blueprints.home import home_bp
    app.register_blueprint(home_bp)

    from .blueprints.tasks import tasks_bp
    app.register_blueprint(tasks_bp)

    return app








# app = Flask(__name__)

# # index variable for tasks list
# index_lists = 1
# # index variable for tasks
# index_tasks = 1
# # index variable for remove and edit list
# index = 1

# # lists variable
# task_list = {}
# tasks_list = {}
# task_list['tasks'] = []

# # tasks variable
# task = {}
# tasks = {}


# # login templates
# @ app.route('/')
# def login():
#     if request.method == 'GET':
#         return render_template('login/login.html')
#     else:
#         #read values from form
#         login = request.form['login']
#         password = request.form['password']
#         print(password,login)
#         print('hello')
#         if login == 'malak' and password == 'mm1234':
        
#             #redirect to home
#             return redirect(url_for('home'))

#         else:
#             return render_template('login/login.html')



# # base of the all pages
# @ app.route('/base')
# def base():
#     return render_template('page/base.html')

# # home page that contain existing lists


# @ app.route('/home')
# def home():
#     return render_template('page/home.html', tasks_list=tasks_list, tasks=tasks)

# # create a new list


# @ app.route('/newlist', methods=['POST', 'GET'])
# def new_list():
#     global index_lists
#     if request.method == 'GET':
#         return render_template('list/new-list.html')
#     else:
#         time = datetime.now()
#         list_name = request.form['list_name']
#         task_list['name'] = list_name
#         task_list['created_at'] = time
#         task_list['last_update'] = time
#         print(time)
#         tasks_list[index_lists] = task_list.copy()
#         index_lists += 1
#         return redirect('home')

# # add new task


# @ app.route('/newtask', methods=['POST', 'GET'])
# def new_task():
#     global index_tasks, tasks_list
#     if request.method == 'GET':
#         return render_template('task/new-task.html', tasks_list=tasks_list)
#     else:
#         time = datetime.now()
#         task_name = request.form['task_name']
#         status = request.form['status']
#         priority = request.form['priority']
#         description = request.form['description']
#         assigned_list = request.form['assigned_list']

#         task['name'] = task_name
#         task['created_at'] = time
#         task['status'] = status
#         task['priority'] = priority
#         task['description'] = description
#         task['last_update'] = time
#         tasks[index_tasks] = task.copy()
#         index_tasks += 1

#         for tasklist in tasks_list.values():
#             if tasklist['name'] == assigned_list:
#                 tasklist['tasks'].append(task.copy())

#         return redirect(url_for('home'))

# # view details for a list


# @ app.route('/list/view/<int:index>')
# def view_list(index):
#     view_list = tasks_list[index]
#     return render_template('list/view-list.html', view_list=view_list)

# # view details for a task
# @ app.route('/task/view/<int:index>')
# def view_task(index):
#     view_task = tasks[index]
#     return render_template('task/view-task.html', view_task=view_task)

# # remove specific list
# @ app.route('/list/remove/<int:index>')
# def remove_list(index):
#     global tasks_list
#     del tasks_list[index]
#     return render_template('home.html', tasks_list=tasks_list, tasks=tasks)

# # remove specific task
# @ app.route('/task/remove/<int:index>')
# def remove_task(index):
#     global tasks
#     del tasks[index]
#     return render_template('page/home.html', tasks_list=tasks_list, tasks=tasks)


# # edit name of the list
# @ app.route('/list/edit/<int:index>', methods=['GET', 'POST'])
# def edit_list(index):
#     if request.method == 'GET':
#         view_list = tasks_list[index]
#         return render_template('list/edit-list.html', view_list=view_list)
#     else:
#         last_update = datetime.now()
#         name = request.form['new_name']
#         tasks_list[index]['name'] = name
#         tasks_list[index]['last_update'] = last_update

#         return redirect(url_for('home'))


# # edit task
# @ app.route('/task/edit/<int:index>', methods=['GET', 'POST'])
# def edit_task(index):
#     if request.method == 'GET':
#         view_task = tasks[index]
#         return render_template('task/edit-task.html', view_task=view_task)
#     else:
#         name = request.form['new_name']
#         status = request.form['new_status']
#         priority = request.form['new_priority']
#         description = request.form['new_description']
#         last_update = datetime.now()

#         tasks[index]['name'] = name
#         tasks[index]['status'] = status
#         tasks[index]['priority'] = priority
#         tasks[index]['description'] = description
#         tasks[index]['last_update'] = last_update

#         return redirect(url_for('home'))
