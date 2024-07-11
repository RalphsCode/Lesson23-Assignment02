from flask import Flask, render_template, jsonify 
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Cupcake
# Need Flask to start a server
# Need SQLAlchemy for the Models


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ponderosa@localhost/cupcakes'

with app.app_context():
    connect_db(app)
    db.create_all()

def serialize(cupcake):
    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "rating": cupcake.rating,
        "image": cupcake.image
    }

@app.route('/')
def home():
    cupcakes = Cupcake.query.all()
    return render_template('home.html', cupcakes=cupcakes)
 
@app.route('/api/cupcakes')
def all_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized = [serialize(cupcake) for cupcake in cupcakes]

    return (jsonify(cupcakes=serialized), 200)

@app.route('/api/cupcakes/<int:id>')
def view_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    serialized = [serialize(cupcake)]
    return (jsonify(cupcake=serialized), 200)