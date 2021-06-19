from flask import Flask, redirect, render_template, request, jsonify
# from pymongo import MongoClinet
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()

app = Flask(__name__)

# client = MongoClinet(os.environ.get("MONGODB_URI"))
# app.db = client.todolist

# @app.route('/')
# def index():
#     return 'This mother fucker'


conn = sqlite3.connect('todo.db')

def create_table():
    with conn:
        cursor = conn.cursor()
        cursor.execute('''
            create table if not exists todo(
                id integer primary key autoincrement,
                project text,
                task text,
                description text
            )
            
            ''')

def insertstart():
    with conn:
        cursor = conn.cursor()
        insert_statement = '''
        insert into todo(project, task, description) values
        ('project 1', 'task1', 'description1'),
        ('project 1', 'task2', 'description2'),
        ('project 1', 'task3', 'description3'),
        ('project 1', 'task4', 'description4'),
        ('project 2', 'task1', 'description1'),
        ('project 2', 'task2', 'description1'),
        ('project 2', 'spisof', 'description1'),
        ('project 2', 'asdsf', 'description1'),
        ('project 2', 'okay', 'description1'),
        ('project 3', 'task1', 'description1'),
        ('project 3', 'task1654', 'description1'),
        ('project 4', 'do something', 'description1'),
        ('project 5', 'task1', 'big sl sleks aseofpiase ase;lkfase ;lasm;elfkas;lk efma;sleewlfk we oiutherio krtjkler t ewrthjer;lk ewlr;kgj eroigjaher gvlkrdjgh dr'),
        ('project 6', 'task1', 'this sie a ske asddfkjasen ase aseuisaeiu fasek afsjuasefiu asefiul asefiuahgse fja,sefhb akjsehf '),
        ('project 7', 'task1', 'description1')
'''
        cursor.execute(insert_statement)


@app.route('/', methods=['GET'])
def get_all_records():
    conn = sqlite3.connect('todo.db')
    with conn:
        cursor = conn.cursor()
        statement = 'select id, project, task, description from todo'
        cursor.execute(statement)
        records = cursor.fetchall()
    return render_template('index.html', records=records)



@app.route('/<id>', methods=['GET'])
def get_record_by_id(id):
    conn = sqlite3.connect('todo.db')
    with conn:
        cursor = conn.cursor()
        statement = 'select id, project, task, description from todo where id = ?'
        cursor.execute(statement, [id])
        records = cursor.fetchall()
    return render_template('index.html', records=records)
    
    

@app.route('/', methods=['POST'])
def insert_record(project, task, description):
    with conn:
        cursor = conn.cursor()
        statement = 'insert into todo(project, task, description) values (?, ?, ?)'
        cursor.execute(statement, [project, task, description])




if __name__ == '__main__':
    create_table()
    insertstart()
    app.run(host='127.0.0.1', port=8080, debug=True)
