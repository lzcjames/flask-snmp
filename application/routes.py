from application import app
from flask import Flask, render_template

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
    return render_template("user.html",users=users,isAdmin=isAdmin)
