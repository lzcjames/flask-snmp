from application import app
from flask import Flask, render_template
from .backend.dto.Material import Material
@app.route('/<isAdmin>')
def hello_name(isAdmin):
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
    m1 = Material("toto","192.168.1.1",["ee","aa"])
    return render_template("user.html",users=users,isAdmin=isAdmin,ip= m1.ip)
