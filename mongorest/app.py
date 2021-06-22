import os

import dotenv
import pymongo
from flask import Flask, jsonify, redirect, render_template, request
from bson.json_util import dumps

from . import mongodb
from . import sqlitedb

dotenv.load_dotenv()


CLIENT = pymongo.MongoClient('mongodb://127.0.0.1:27017')
# CLIENT = pymongo.MongoClient(os.environ.get('MONGODB_AWS'))
# CLIENT = pymongo.MongoClient(os.environ.get('MONGODB_ATLAS'))
DATABASE = os.environ.get('DATABASE')
COLLECTION = os.environ.get('COLLECTION')
db = mongodb.DBManager(client=CLIENT, database=DATABASE, collection=COLLECTION)
# db = sqlitedb.DBManager(db_name='todo.db')

app = Flask(__name__)

# db.insert_test_values(50)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/employee/')
def get_employees():
    employees = db.get_employee_list()
    return dumps({'employees': employees})


@app.route('/employee/<int:id>/')
def employee_by_id(id):
    employee = db.get_employee_id(id)
    return dumps({'employee': employee})


@app.route('/role/')
def get_roles():
    roles = db.get_role_list()
    return dumps({'roles': roles})


@app.route('/role/<string:name>/')
def role_by_name(name):
    '''Find employees with this role'''
    roles = db.get_role_employees(name)
    return dumps({name: roles})


@app.route('/department/')
def get_departments():
    departments = db.get_department_list()
    return dumps({'departments': departments})


@app.route('/department/<string:name>/')
def department_by_name(name):
    '''Find employees with this department'''
    departments = db.get_department_employees(name)
    return dumps({name: departments})


# def todo_list():
#     if request.method == 'POST':
#         project = request.form.get('project')
#         task = request.form.get('task')
#         description = request.form.get('description')
#         db.insert(project, task, description)

#     records = db.get_employee_list()
#     return render_template('index.html', records=records)
