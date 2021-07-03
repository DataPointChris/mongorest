import os
import dotenv
import pymongo
from bson.json_util import dumps as bson_dumps
from flask import Flask, make_response, render_template, request

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
            # db.delete_all()
            db.insert_test_values(numemps)
        if delete:
            db._delete_all()
    employee_list = db.get_employee_directory()
    employees = []
    for employee in employee_list:
        first = employee.get('firstname')
        last = employee.get('lastname')
        empid = employee.get('empid')
        string = f'EMPID: {empid}, Name: {first} {last}'
        employees.append(string)
    depts = db.get_aggregated_departments()
    departments = [{d.get('_id').capitalize(): d.get('emps')} for d in depts]

    role_list = db.get_aggregated_roles()
    roles = [{d.get('_id').capitalize(): d.get('emps')} for d in role_list]
    return render_template(
        'index.html', employees=employees, departments=departments, roles=roles
    )


@app.route('/api/')
def api():
    return render_template('api.html')


# -------------------- API ENDPOINTS -------------------- #


# ----- EMPLOYEES ----- #


@app.route('/api/employees/', methods=['GET', 'POST'])
def employees():
    if request.method == 'POST':
        employee = request.get_json()
        response = db.post_new_employee(employee)
        status = 201
        headers = {'content-type': 'application/json'}
        return make_response(bson_dumps(response), status, headers)

    response = db.get_employee_directory()
    status = 200
    headers = {'content-type': 'application/json'}
    return make_response(bson_dumps(response), status, headers)


@app.route('/api/employees/<int:empid>/', methods=['GET', 'PUT', 'DELETE'])
def employee_by_empid(empid):
    '''empid comes from URL, no need to put it in the payload'''
    updated = request.get_json()
    if request.method == 'PUT':
        db.put_update_employee_by_empid(empid, **updated)
        response = db.get_employee_by_empid(empid)
        status = 200
        headers = {'content-type': 'application/json'}
        return make_response(bson_dumps(response), status, headers)

    elif request.method == 'DELETE':
        db.delete_employee_by_empid(empid)
        status = 204  # no content
        return make_response('', status)

    response = db.get_employee_by_empid(empid)
    status = 200
    headers = {'content-type': 'application/json'}
    return make_response(bson_dumps(response), status, headers)


# ----- ROLES ----- #


@app.route('/api/roles/', methods=['GET'])
def roles():
    response = db.get_role_list()
    status = 200
    headers = {'content-type': 'application/json'}
    return make_response(bson_dumps(response), status, headers)


@app.route('/api/roles/<string:name>/', methods=['PUT'])
def edit_role(name):
    updated = {'updates': request.get_json()}
    db.put_edit_role_by_name(name, updated)
    return make_response('Successful update', 200)


@app.route('/api/roles/<string:name>/employees/', methods=['GET'])
def employees_by_role(name):
    '''Find employees with this role'''
    response = db.get_employees_by_role(name)
    status = 200
    headers = {'content-type': 'application/json'}
    return make_response(bson_dumps(response), status, headers)


@app.route('/api/roles/<string:name>/departments/', methods=['GET'])
def departments_by_role(name):
    '''Find departments with this role'''
    response = db.get_departments_with_role(name)
    status = 200
    headers = {'content-type': 'application/json'}
    return make_response(bson_dumps(response), status, headers)


# ----- DEPARTMENTS ----- #


@app.route('/api/departments/', methods=['GET'])
def departments():
    response = db.get_department_list()
    status = 200
    headers = {'content-type': 'application/json'}
    return make_response(bson_dumps(response), status, headers)


@app.route('/api/departments/<string:name>/', methods=['PUT'])
def edit_department(name):
    updated = {'updates': request.get_json()}
    db.put_edit_department_by_name(name, **updated)
    return make_response('Successful update', 200)


@app.route('/api/departments/<string:name>/employees/', methods=['GET'])
def employees_by_department(name):
    '''Find employees with this department'''
    response = db.get_employees_in_department(name)
    status = 200
    headers = {'content-type': 'application/json'}
    return make_response(bson_dumps(response), status, headers)


@app.route('/api/departments/<string:name>/roles/', methods=['GET'])
def roles_by_department(name):
    '''Find roles in this department'''
    response = db.get_roles_by_department(name)
    status = 200
    headers = {'content-type': 'application/json'}
    return make_response(bson_dumps(response), status, headers)
