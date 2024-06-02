from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB client setup
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['profiles']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert_data():
    name = request.form['name']
    email = request.form['email']

    if name and email:
        document = {"name": name, "email": email}
        collection.insert_one(document)
        return redirect('/')
    else:
        return "Name and email are required."

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
