from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# we need some configurations b4 instantiate SQL Alchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #to restrict any warning messages, when running the app.
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///db.sqlite" # Location of the database.
# SQLite is a database, which is a file on our system
db = SQLAlchemy(app)


#CREATE A TABLE IN THE DATABASE
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))

#Add data to db
@app.route('/', methods = ['GET','POST'])
def index():
    name = ''
    location = ''
    if request.method == 'POST' and 'fname' and 'loc' in request.form:
        name = request.form.get('fname')
        location = request.form.get('loc')
        user = User(name = name, location = location)
        db.session.add(user)
        db.session.commit()
    return render_template("alchemy.html", name = name, location = location)


app.run()
