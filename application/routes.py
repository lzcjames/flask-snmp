from flask_sqlalchemy import SQLAlchemy
from application import app
from flask import Flask, render_template, request
from .backend.dto.Material import Material
from .backend.service.OperatorSnmp import OperatorSnmp
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
    result = OperatorSnmp.getResultSnmp('192.168.1.1','1.3.6.1.1.2.1.0')
    results =[]
    
    for i in range(10):
        results.append(result) 

    length = len(results)
    return render_template("user.html",results = results, length = length)

@app.route('/sendto_form/<name>')
def sendto_form(name):
    materialToModify = OperatorSnmp.get(name)
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
    OperatorSnmp.add(m1Json)
    return m1.name

@app.route('/update/<int:id>', methods=['POST'])
def update_data(id):
    name = request.form['name']
    ip = request.form['ip']
    mac = request.form['mac']
    interface = request.form['interface']
    date = request.form['date']
    status = request.form['status']
    
    m1 = Material(name,ip,mac,interface,date,status,"1.3.6.1.1.2.1.1")
    m1Json = jsonpickle.encode(m1)
    res = OperatorSnmp.update(m1Json,id)
    return res


@app.route('/delete/<int:id>')
def delete_data(id):
    res = OperatorSnmp.delete(id)
    return res

@app.route('/get_data', methods=['GET'])
def get_data():
    materials = jsonpickle.decode((OperatorSnmp.getAll()))
    return render_template("user.html",materials = materials, get_data=True)