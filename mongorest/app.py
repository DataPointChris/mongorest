from flask import Flask, redirect, render_template, request, jsonify
from pymongo import MongoClinet
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = MongoClinet(os.environ.get("MONGODB_URI"))
app.db = client.mydb

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        db_entry = request.form.get('form_entry')
        app.db.mydb.insert({'record'})

    records = [
        (record['field1'], record['field2']) for record in app.db.entries.find({})
    ]

    return render_template('index.html', records=records)

