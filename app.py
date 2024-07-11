from flask import Flask, render_template  
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Cupcake
# Need Flask to start a server
# Need SQLAlchemy for the Models


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ponderosa@localhost/cupcakes'

with app.app_context():
    connect_db(app)
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')
 
