from flask import Flask, render_template,request,session,redirect,url_for
from flask_mail import Message,Mail
import mysql.connector
app = Flask(__name__)
app.secret_key='super-secret-key'
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'parthprecise11@gmail.com',
	MAIL_PASSWORD = '8619130803'
	)
mail = Mail(app)

@app.route("/<xx>")
def home(xx):
    print("     "+xx+"   c ool ts working")
    session['logged_in'] = True
    if session.get('logged_in'):
        print(session.get('logged_in'))
        return render_template('register.html')
    else:
        return render_template('index.html')

@app.route("/register")
def gh():
    print(session.get('logged_in'))
    return render_template('index.html')

@app.route("/gfdg")
def code():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="bugtracking"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT name FROM userid")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x[0])
    return render_template('index.html')


@app.route("/register")
def register():
    try:
        msg = Message("Send Mail Tutorial!",
                      sender="parthprecise11@gmail.com",
                      recipients=["parthdarak11@email.com"])
        msg.body = "Yo!\nHave you heard the good word of Python???"
        mail.send(msg)
        return 'Mail sent!'
    except:
        return 'Mail not sent'


@app.route("/xyz",methods=["POST","GET"])
def code1():
    uname=request.form['userName']
    return redirect(url_for('code'))

app.run(debug=True)

# @app.route("/about")
# def codePlanet():
#     name = "CodePlanet"
#     return render_template('about.html', name2= name)
#
# @app.route("/new")
# def bootstrap():
#     return render_template('fg.html')

#app.run(debug=True)