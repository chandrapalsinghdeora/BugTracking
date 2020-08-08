from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/bugtracking'
db = SQLAlchemy(app)


class userid(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    Pk_userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    name1 = db.Column(db.String(50), nullable=False)


@app.route("/")
def home():
    return render_template('register.html')


@app.route("/cdz")
def cdz():
    return render_template('about.html')


@app.route("/xyz", methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('userName')
        entry = userid(name=name,name1=email )
        db.session.add(entry)
        db.session.commit()
    return render_template('about.html')


app.run(debug=True)

