from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request, session
from application import app
from application import db
from.backend.dto.User import User
from flask import Flask, render_template, request
from.backend.dto.Material import Material
from.backend.service.OperatorMaterial import OperatorMaterial
from.backend.service.OperatorSnmp import OperatorSnmp
from.backend.service.OperatorView import OperatorView
from.backend.service.OperatorUser import OperatorUser
import jsonpickle
import json
import pygal
import datetime
import os
import json
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html', logininfo = "please login")
    else :
        return render_template("user.html", admin = session.get('logged_in_admin'))

@app.route('/to_form/<name>')
def to_form(name):
    materialToModify = OperatorMaterial.get(name)
    if not session.get('logged_in'):
        return render_template('login.html', logininfo = "please login")
    else :
        return render_template("user.html", get_form = True, materialToModify = materialToModify, admin = session.get('logged_in_admin'))

@app.route('/get_form')
def get_form():
    if not session.get('logged_in'):
        return render_template('login.html', logininfo = "please login")
    else :
        return render_template("user.html", get_form = True, admin = session.get('logged_in_admin'))

@app.route('/add_data', methods = ['POST'])
def add_data():
    name = request.form['name']
    ip = request.form['ip']
    mac = request.form['mac']
    interface = request.form['interface']
    date = request.form['date']
    community = request.form['community']

    m1 = Material(name, ip, mac, interface, date, community)
    m1Json = jsonpickle.encode(m1)
    OperatorMaterial.add(m1Json)
    return get_data()

@app.route('/update_data/<int:id>', methods = ['POST'])
def update_data(id):
    name = request.form['name']
    ip = request.form['ip']
    mac = request.form['mac']
    interface = request.form['interface']
    date = request.form['date']
    community = request.form['community']

    m1 = Material(name, ip, mac, interface, date, community)
    m1Json = jsonpickle.encode(m1)
    res = OperatorMaterial.update(m1Json, id)
    return get_data()

@app.route('/delete_data/<int:id>')
def delete_data(id):
    if not session.get('logged_in_admin'):
        return render_template("login.html", logininfo="please login before you delete data" )
    else :
        res = OperatorMaterial.delete(id)
        return get_data()

@app.route('/get_data', methods = ['GET'])
def get_data():
    materials = jsonpickle.decode((OperatorMaterial.getAll()))
    if not session.get('logged_in'):
        return render_template('login.html', logininfo = "please login")
    else :
        return render_template("user.html", materials = materials, get_data = True, admin = session.get('logged_in_admin'))

@app.route('/get_log_event', methods = ['GET'])
def get_log_event():
    events = jsonpickle.decode((OperatorView.getLogEvent()))
    if not session.get('logged_in'):
        return render_template('login.html', logininfo = "please login")
    else :
        return render_template("user.html", events = events, get_log_event = True, admin = session.get('logged_in_admin'))

@app.route('/export_event')
def export_event():
    events = jsonpickle.decode((OperatorView.getLogEvent()))
    time = datetime.datetime.now().strftime("%Y-%m-%d")
    
    filename = 'Event-'+time+'.log'
    new_file_path = os.path.join('./Export/', filename) # the default path is project root path
    
    if not session.get('logged_in'):
        return render_template("login.html", logininfo="please login before you export data" )
    else :
        with open(new_file_path,mode='w', buffering=-1, 
        encoding='utf-8', errors=None, newline=None, 
        closefd=True, opener=None) as f:
            for strEvent in events:
                f.writelines(str(strEvent)+"\n")
            f.close()
        return render_template("user.html")

@app.route('/export_record')
def export_record():
    dictReocrd = OperatorView.exportLogRecord()
    time = datetime.datetime.now().strftime("%Y-%m-%d")
    
    filename = 'Record-'+time+'.json'
    new_file_path = os.path.join('./Export/', filename) # the default path is project root path
    
    if not session.get('logged_in'):
        return render_template("login.html", logininfo="please login before you export data" )
    else :
        with open(new_file_path,mode='w', buffering=-1, 
        encoding='utf-8', errors=None, newline=None, 
        closefd=True, opener=None) as f:
            f.write(json.dumps(dictReocrd, indent=4))
            f.close()
        return render_template("user.html")

@app.route('/export_conf')
def export_conf():
    dictMaterial = OperatorView.getConf()
    time = datetime.datetime.now().strftime("%Y-%m-%d")
    
    filename = 'Conf-'+time+'.json'
    new_file_path = os.path.join('./Export/', filename) # the default path is project root path
    
    if not session.get('logged_in'):
        return render_template("login.html", logininfo="please login before you export data" )
    else :
        with open(new_file_path,mode='w', buffering=-1, 
        encoding='utf-8', errors=None, newline=None, 
        closefd=True, opener=None) as f:
            f.write(json.dumps(dictMaterial, indent=4))
            f.close()
        return render_template("user.html")

@app.route('/get_log_record', methods = ['GET'])
def get_log_record():
    records = jsonpickle.decode((OperatorView.getLogRecord()))
    if not session.get('logged_in'):
        return render_template('login.html', logininfo = "please login")
    else :
        return render_template("user.html", records = records, get_log_record = True, admin = session.get('logged_in_admin'))

# Route for handling the login page logic
@app.route('/login', methods = ['POST'])
def login():
    logininfo = None
    username = (request.form['username'])
    password = (request.form['password'])
    dbUser = OperatorUser.login(username)
    
    if username == dbUser.login and password == dbUser.password:
        session['logged_in'] = True
        if dbUser.admin:
            session['logged_in_admin'] = True
        return render_template("user.html", admin = session.get('logged_in_admin'))
    else :
        return render_template('login.html', logininfo = 'Invalid Credentials.Please try again.')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['logged_in_admin'] = False
    return render_template('login.html', logininfo = 'Account has been logged out')

@app.route('/get_SnmpText', methods = ['GET'])
def get_SnmpText():
    ip = request.args.get('ip')
    name = request.args.get('name')
    records = jsonpickle.decode(OperatorSnmp.getRecordsbyNameAndDate(name))
    if not session.get('logged_in'):
        return render_template('login.html', logininfo = "please login")
    else :
        return render_template("user.html", materialname = name, records = records, get_tabSnmp = True, admin = session.get('logged_in_admin'))

@app.route('/get_SnmpGraph/', methods = ['GET'])
def get_SnmpGraph():
    try:
        name = request.args.get('name')
        ifname = request.args.get('ifname')
        records = jsonpickle.decode(OperatorSnmp.getRecordsbyNameAndIfname(name,ifname))
        times = []
        inOctects = []
        outOctects = []
        for r in records:
            times.append(r.timestamp)
            inOctects.append(r.inoctects)
            outOctects.append(r.outoctects)

        graphInOctects = pygal.Line()
        graphInOctects.title = "Détail de l'interface "+ifname
        graphInOctects.x_labels = times
        print(inOctects)
        graphInOctects.add('In Octects', inOctects)
        graphInOctects.add('Out Octects', outOctects)
        graph_data_inOctects = graphInOctects.render_data_uri()
        return render_template("user.html", graph_data_inOctects = graph_data_inOctects)
    except Exception as e:
        return (str(e))