from flask import Flask, render_template


app = Flask(__name__,template_folder='./frontend/templates',static_folder='./frontend/static')

@app.route('/<role>')
def hello_name(role):
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
    return render_template("user.html",users=users,role=role)



