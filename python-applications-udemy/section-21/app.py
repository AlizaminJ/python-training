from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy#
#from flask.ext.sqlalchemy import SQLAlchemy # depreciated
from send_email import send_email
from sqlalchemy.sql import func         
# With Flask it is mainly used SQLAlchemy which higher level than psycopg2. 
# The main advantage you do not have to do repetitive tasks like establish, commit and close with SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_

# After creating  database in pgAdmin manually, run the following code in commandline to create a table in datab
# Go to the directory
#python
#from app import db
#db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        print(email, height)
        if db.session.query(Data).filter(Data.email_ == email).count()== 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height, 1)
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            print(average_height)
            return render_template("success.html")
    return render_template('index.html', text="Seems like we got something from that email once!")

if __name__ == '__main__':
    app.debug=True
    app.run(port=5005)
