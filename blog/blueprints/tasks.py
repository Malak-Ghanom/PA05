from flask import Blueprint, render_template,request ,redirect,session,url_for
import sqlite3
from datetime import datetime
from .home import task_list,tasks,task,tasks_list,index,index_lists,index_tasks


tasks_bp = Blueprint('tasks', __name__)

# add new task
@ tasks_bp.route('/newtask', methods=['POST', 'GET'])
def new_task():
    global index_tasks, tasks_list
    if request.method == 'GET':
        return render_template('task/new-task.html', tasks_list=tasks_list)
    else:
        time = datetime.now()
        task_name = request.form['task_name']
        status = request.form['status']
        priority = request.form['priority']
        description = request.form['description']
        assigned_list = request.form['assigned_list']

        task['name'] = task_name
        task['created_at'] = time
        task['status'] = status
        task['priority'] = priority
        task['description'] = description
        task['last_update'] = time
        tasks[index_tasks] = task.copy()
        index_tasks += 1

        for tasklist in tasks_list.values():
            if tasklist['name'] == assigned_list:
                tasklist['tasks'].append(task.copy())

        return redirect(url_for('home.home'))


# remove specific task
@ tasks_bp.route('/task/remove/<int:index>')
def remove_task(index):
    global tasks
    del tasks[index]
    return render_template('page/home.html', tasks_list=tasks_list, tasks=tasks)


# edit task
@tasks_bp.route('/task/edit/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    if request.method == 'GET':
        view_task = tasks[index]
        return render_template('task/edit-task.html', view_task=view_task)
    else:
        name = request.form['new_name']
        status = request.form['new_status']
        priority = request.form['new_priority']
        description = request.form['new_description']
        last_update = datetime.now()

        tasks[index]['name'] = name
        tasks[index]['status'] = status
        tasks[index]['priority'] = priority
        tasks[index]['description'] = description
        tasks[index]['last_update'] = last_update

        return redirect(url_for('home'))

# view details for a task
@tasks_bp.route('/task/view/<int:index>')
def view_task(index):
    view_task = tasks[index]
    return render_template('task/view-task.html', view_task=view_task)
