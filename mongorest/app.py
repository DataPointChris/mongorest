from locale import Error
import os

import dotenv
import pymongo
from flask import Flask, jsonify, redirect, render_template, request
from bson.json_util import dumps

from . import mongodb

dotenv.load_dotenv()


CLIENT = pymongo.MongoClient(os.environ.get('MONGODB_LOCAL'))
# CLIENT = pymongo.MongoClient(os.environ.get('MONGODB_AWS'))
DATABASE = os.environ.get('DATABASE')
COLLECTION = os.environ.get('COLLECTION')
db = mongodb.DBManager(client=CLIENT, database=DATABASE, collection=COLLECTION)

app = Flask(__name__)

# -------------------- HTML -------------------- #


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        insert = request.form.get('insertfake')
        try:
            numemps = int(request.form.get('numemps'))
        except TypeError:
            numemps = 1
        delete = request.form.get('deleteall')
        if insert:
            db.delete_all()
            db.insert_test_values(numemps)
        if delete:
            db.delete_all()
    emps = db.get_employee_directory()
    employees = [(f'{d["firstname"]} {d["lastname"]}') for d in emps]
    return render_template('index.html', employees=employees)


@app.route('/api/')
def api():
    return render_template('api.html')


# -------------------- API ENDPOINTS -------------------- #


# ----- EMPLOYEES ----- #


@app.route('/api/employees/', methods=['GET', 'POST'])
def employees():
    if request.method == 'POST':
        employee = request.get('employee')
        db.post_new_employee(employee)
        # TODO: Do I need a success message here?
        return render_template('index.html')

    employees = db.get_employee_directory()
    # TODO: Should this be a make_response
    return dumps({'employees': employees})


@app.route('/api/employees/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def employee_by_id(id):
    if request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass

    employee = db.get_employee_by_id(id)
    # TODO: Should this be a `make_response()`
    return dumps({'employee': employee})


# ----- ROLES ----- #


@app.route('/api/roles/', methods=['GET'])
def roles():
    roles = db.get_role_list()
    # TODO: make_response
    return dumps({'roles': roles})


@app.route('/roles/<string:name>/', methods=['PUT'])
def edit_role(name):
    db.put_edit_role_by_name()


@app.route('/roles/<string:name>/employees/', methods=['GET'])
def employees_by_role(name):
    '''Find employees with this role'''
    roles = db.get_employees_by_role(name)
    return dumps({name: roles})


@app.route('/roles/<string:name>/departments', methods=['GET'])
def departments_by_role(name):
    '''Find departments with this role'''
    roles = db.get_departments_with_role(name)
    return dumps({name: roles})


# ----- DEPARTMENTS ----- #


@app.route('/api/departments/', methods=['GET'])
def departments():
    departments = db.get_department_list()
    return dumps({'departments': departments})


@app.route('/api/departments/<string:name>/', methods=['PUT'])
def edit_department(name):
    db.put_edit_department_by_name()


@app.route('/api/departments/<string:name>/employees/', methods=['GET'])
def employees_by_department(name):
    '''Find employees with this department'''
    departments = db.get_employees_in_department(name)
    return dumps({name: departments})


@app.route('/api/departments/<string:name>/roles/', methods=['GET'])
def roles_by_department(name):
    '''Find roles in this department'''
    departments = db.get_roles_by_department(name)
    return dumps({name: departments})
