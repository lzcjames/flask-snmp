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
import pygal

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html', logininfo="please login")
    else:
        return render_template("user.html", admin=session.get('logged_in_admin') )

@app.route('/to_form/<name>')
def to_form(name):
    materialToModify = OperatorMaterial.get(name)
    
    if not session.get('logged_in'):
        return render_template('login.html', logininfo="please login")
    else :
        return render_template("user.html", get_form=True,materialToModify=materialToModify, admin=session.get('logged_in_admin'))

@app.route('/get_form')
def get_form():
    if not session.get('logged_in'):
        return render_template('login.html', logininfo="please login")
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
    community = request.form['community']
    
    m1 = Material(name,ip,mac,interface,date,status,community)
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
    community = request.form['community']

    m1 = Material(name,ip,mac,interface,date,status,community)
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
        return render_template('login.html', logininfo="please login")
    else :
        return render_template("user.html",materials = materials, get_data=True, admin=session.get('logged_in_admin'))

@app.route('/get_log', methods=['GET'])
def get_log():
    events = jsonpickle.decode((OperatorView.getLog()))
    
    if not session.get('logged_in'):
        return render_template('login.html', logininfo="please login")
    else :
        return render_template("user.html",events = events, get_log=True, admin=session.get('logged_in_admin'))

# Route for handling the login page logic
@app.route('/login', methods=['POST'])
def login():
    logininfo = None
    username = (request.form['username'])
    password = (request.form['password'])
    dbUser = OperatorUser.login(username)
    
    if username == dbUser.login and password == dbUser.password :
        session['logged_in'] = True
        if dbUser.admin :
            session['logged_in_admin'] = True
        return render_template("user.html", admin=session.get('logged_in_admin'))
    else:
        return render_template('login.html', logininfo='Invalid Credentials.Please try again.')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['logged_in_admin'] = False
    return  render_template('login.html',logininfo='Account has been logged out')

@app.route('/get_SnmpText',methods=['GET'])
def get_SnmpText():
    ip =  request.args.get('ip')
    name =  request.args.get('name')
    records = jsonpickle.decode(OperatorSnmp.getRecordsbyNameAndDate(name))
    if not session.get('logged_in'):
        return render_template('login.html', logininfo="please login")
    else :
        return render_template("user.html", materialname=name, records=records, get_tabSnmp=True, admin=session.get('logged_in_admin'))
        
@app.route('/get_SnmpGraph/')
def get_SnmpGraph():
	try:
		graph = pygal.Line()
		graph.title = '% Change Coolness of programming languages over time.'
		graph.x_labels = ['2011','2012','2013','2014','2015','2016']
		graph.add('In Octects',  [15, 31, 89, 200, 356, 900])
		graph.add('Out Octects',    [15, 45, 76, 80,  91,  95])
		graph_data = graph.render_data_uri()
		return render_template("user.html", graph_data = graph_data)
	except Exception as e:
		return(str(e))