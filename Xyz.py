from flask_mail import Mail, Message
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

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


@app.route('/send-mail/')
def send_mail():
    msg = Message('Hel9l', sender='parthprecise11@gmail.com', recipients=['parthdarak11@gmail.com'])
    msg.html = render_template('about.html', name='ghgh')
    mail.send(msg)
    return "hello"


@app.route('/hello/')
def hello():
    return "hello welcome"


@app.route('/cds/')
def cds():
    email= request.args.get('email')
	db.session.query(userid)
	q = q.filter(userid.name == email)
	record = q.one()
	record.name1 = 'Azure Radiance'




app.run(debug=True)