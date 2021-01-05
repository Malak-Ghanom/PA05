from flask import Blueprint, render_template,request ,redirect,session,url_for
import sqlite3
from datetime import datetime
from .home import task_list,tasks,task,tasks_list,index,index_lists,index_tasks


lists_bp = Blueprint('lists', __name__)


# view details for a list
@ lists_bp.route('/list/view/<int:index>')
def view_list(index):
    view_list = tasks_list[index]
    return render_template('list/view-list.html', view_list=view_list)


# remove specific list
@ lists_bp.route('/list/remove/<int:index>')
def remove_list(index):
    global tasks_list
    del tasks_list[index]
    return render_template('page/home.html', tasks_list=tasks_list, tasks=tasks)


# edit name of the list
@ lists_bp.route('/list/edit/<int:index>', methods=['GET', 'POST'])
def edit_list(index):
    if request.method == 'GET':
        view_list = tasks_list[index]
        return render_template('list/edit-list.html', view_list=view_list)
    else:
        last_update = datetime.now()
        name = request.form['new_name']
        tasks_list[index]['name'] = name
        tasks_list[index]['last_update'] = last_update

        return redirect(url_for('home.home'))


@ lists_bp.route('/newlist', methods=['POST', 'GET'])
def new_list():
    global index_lists
    if request.method == 'GET':
        return render_template('list/new-list.html')
    else:
        time = datetime.now()
        list_name = request.form['list_name']
        task_list['name'] = list_name
        task_list['created_at'] = time
        task_list['last_update'] = time
        print(time)
        tasks_list[index_lists] = task_list.copy()
        index_lists += 1
        return redirect('home')