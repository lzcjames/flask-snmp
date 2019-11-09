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

@app.route('/handle_data', methods=['POST'])
def handle_data():
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
