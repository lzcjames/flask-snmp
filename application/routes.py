from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request, session   
from application import app
from application import db
from .backend.dto.User import User
from flask import Flask, render_template, request
from .backend.dto.Material import Material
from .backend.service.OperatorMaterial import OperatorMaterial
from .backend.service.OperatorSnmp import OperatorSnmp
from .backend.service.OperatorView import OperatorView
from .backend.service.OperatorUser import OperatorUser
import jsonpickle 


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html', error="please login")
    else:
        return render_template("user.html", admin=session.get('logged_in_admin') )

@app.route('/to_form/<name>')
def to_form(name):
    materialToModify = OperatorMaterial.get(name)
    
    if not session.get('logged_in'):
        return render_template('login.html', error="please login")
    else :
        return render_template("user.html", get_form=True,materialToModify=materialToModify, admin=session.get('logged_in_admin'))

@app.route('/get_form')
def get_form():
    if not session.get('logged_in'):
        return render_template('login.html', error="please login")
    else :
        return render_template("user.html", get_form=True, admin=session.get('logged_in_admin'))

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
    
    if not session.get('logged_in'):
        return render_template('login.html', error="please login")
    else :
        return render_template("user.html",materials = materials, get_data=True, admin=session.get('logged_in_admin'))

@app.route('/get_log', methods=['GET'])
def get_log():
    events = jsonpickle.decode((OperatorView.getLog()))
    
    if not session.get('logged_in'):
        return render_template('login.html', error="please login")
    else :
        return render_template("user.html",events = events, get_log=True, admin=session.get('logged_in_admin'))

@app.route('/get_resultSnmp',methods=['GET'])
def get_resultSnmp():
    ip =  request.args.get('ip', None)
    name =  request.args.get('name', None)
    resultSnmp = {'a':{'status':1,'octects':2},'b':{'status':1,'octects':2},'c':{'status':1,'octects':2}}
    res = OperatorSnmp.getResultSnmp(ip)
    
    if not session.get('logged_in'):
        return render_template('login.html', error="please login")
    else :
        return render_template("user.html", materialname=name, resultSnmp=res, get_tabSnmp=True, admin=session.get('logged_in_admin'))

# Route for handling the login page logic
@app.route('/login', methods=['POST'])
def login():
    error = None
    username = (request.form['username'])
    password = (request.form['password'])
    sqlquery = OperatorUser.login(username)
    
    if username == sqlquery.login and password == sqlquery.password :
        session['logged_in'] = True
        if sqlquery.admin :
            session['logged_in_admin'] = True
        return render_template("user.html", admin=session.get('logged_in_admin'))
    else:
        error = 'Invalid Credentials. Please try again.'
        return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['logged_in_admin'] = False
    return  render_template('login.html')