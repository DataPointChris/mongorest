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


@app.route('/json/')
def get_todos_json():
    todos = db.get_all()
    return dumps({'todos': todos})


@app.route('/', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'POST':
        project = request.form.get('project')
        task = request.form.get('task')
        description = request.form.get('description')
        db.insert(project, task, description)

    records = db.get_all()
    return render_template('index.html', records=records)


@app.route('/<int:id>', methods=['GET'])
def get_task_by_id(id):
    records = db.get_by_id(id)
    return render_template('index.html', records=records)


@app.route('/projects/')
def get_projects_json():
    projects = db.get_projects()
    return dumps({'projects': projects})


if __name__ == '__main__':
    # db.insert_test_values()

