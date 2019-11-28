from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request
from application import app
from application import db
from .backend.dto.User import User
from flask import Flask, render_template, request
from .backend.dto.Material import Material
from .backend.service.OperatorMaterial import OperatorMaterial
from .backend.service.OperatorView import OperatorView
from .backend.service.OperatorUser import OperatorUser
import jsonpickle 



@app.route('/<isAdmin>')
def hello(isAdmin):
    users = [ # fake data from database
        {
            'info': { 'nickname': 'John', 'admin': False },
            'body': 'I am operator!'
        },
        {
            'info': { 'nickname': 'Susan', 'admin': True },
            'body': 'I am administrator!'
        }
    ]
    m1 = Material("toto","192.168.1.1","zez","v","d","s",["ee","aa"])
    return render_template("user.html",users=users,isAdmin=isAdmin,ip= m1.ip)

@app.route('/')
def index():
    result = OperatorMaterial.getResultSnmp('192.168.1.1','1.3.6.1.1.2.1.0')
    results =[]
    
    for i in range(10):
        results.append(result) 

    length = len(results)
    return render_template("user.html",results = results, length = length)

@app.route('/to_form/<name>')
def to_form(name):
    materialToModify = OperatorMaterial.get(name)
    return render_template("user.html", get_form=True,materialToModify=materialToModify)

@app.route('/get_form')
def get_form():
    return render_template("user.html", get_form=True)

@app.route('/add_data', methods=['POST'])
def add_data():
    name = request.form['name']
    ip = request.form['ip']
    mac = request.form['mac']
    interface = request.form['interface']
    date = request.form['date']
    status = request.form['status']
    
    m1 = Material(name,ip,mac,interface,date,status,"1.3.6.1.1.2.1.1")
    m1Json = jsonpickle.encode(m1)
    OperatorMaterial.add(m1Json)
    return get_data()

@app.route('/update_data/<int:id>', methods=['POST'])
def update_data(id):
    name = request.form['name']
    ip = request.form['ip']
    mac = request.form['mac']
    interface = request.form['interface']
    date = request.form['date']
    status = request.form['status']
    
    m1 = Material(name,ip,mac,interface,date,status,"1.3.6.1.1.2.1.1")
    m1Json = jsonpickle.encode(m1)
    res = OperatorMaterial.update(m1Json,id)
    return get_data()


@app.route('/delete_data/<int:id>')
def delete_data(id):
    res = OperatorMaterial.delete(id)
    return get_data()

@app.route('/get_data', methods=['GET'])
def get_data():
    materials = jsonpickle.decode((OperatorMaterial.getAll()))
    return render_template("user.html",materials = materials, get_data=True)

@app.route('/get_log', methods=['GET'])
def get_log():
    events = jsonpickle.decode((OperatorView.getLog()))
    return render_template("user.html",events = events, get_log=True)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        sqlquery = OperatorUser.getUser((request.form['username']))
        if request.form['username'] == sqlquery.login or request.form['password'] == sqlquery.password :
            print(sqlquery.admin)
            return render_template("user.html", admin=sqlquery.admin)
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)