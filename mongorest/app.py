from locale import Error
import os

import dotenv
import pymongo
from flask import Flask, jsonify, redirect, render_template, request
from bson.json_util import dumps

from . import mongodb
from . import sqlitedb

dotenv.load_dotenv()


CLIENT = pymongo.MongoClient(os.environ.get('MONGODB_LOCAL'))
# CLIENT = pymongo.MongoClient(os.environ.get('MONGODB_AWS'))
DATABASE = os.environ.get('DATABASE')
COLLECTION = os.environ.get('COLLECTION')
db = mongodb.DBManager(client=CLIENT, database=DATABASE, collection=COLLECTION)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        insert = request.form.get('insertfake')
        try:
            numemps = int(request.form.get('numemps'))
        except TypeError:
            numemps = 1
        delete = request.form.get('deleteall')
        print(insert, numemps, delete)
        if insert:
            db.delete_all()
            db.insert_test_values(numemps)
        if delete:
            db.delete_all()
    emps = db.get_employee_list()
    employees = [(f'{d["firstname"]} {d["lastname"]}') for d in emps]
    return render_template('index.html', employees=employees)


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
