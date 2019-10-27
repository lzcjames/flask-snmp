from application import app
from flask import Flask, render_template
from .backend.dto.Material import Material
from .backend.service.OperatorSnmp import OperatorSnmp

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

@app.route('/tab')
def tab():
   
    return render_template("test.html")
