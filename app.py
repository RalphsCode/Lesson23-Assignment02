from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Cupcake
from forms import AddCupcake
# Need Flask to start a server
# Need SQLAlchemy for the Models


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ponderosa@localhost/cupcakes'
app.config['SECRET_KEY'] = "RalphsCode123"

with app.app_context():
    connect_db(app)
    db.create_all()

def serialize(cupcake):
    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }

@app.route('/')
def home():
    cupcakes = Cupcake.query.all()
    form = AddCupcake()
    return render_template('home.html', cupcakes=cupcakes, form=form)
 
@app.route('/api/cupcakes', methods=["GET", "POST"])
def all_cupcakes():
    if request.method != "POST":
        cupcakes = Cupcake.query.all()
        serialized = [serialize(cupcake) for cupcake in cupcakes]
        return (jsonify(cupcakes=serialized), 200)
    else:
        flavor = request.json["flavor"]
        size = request.json["size"]
        rating = float(request.json["rating"])
        image = request.json["image"]

        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

        db.session.add(new_cupcake)
        db.session.commit()

        serialized = serialize(new_cupcake)
        return (jsonify(cupcake=serialized), 201)

@app.route('/api/cupcakes/<int:id>', methods=(["GET","PATCH", "DELETE"]))
def view_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    if request.method == "GET":
        serialized = [serialize(cupcake)]
        return (jsonify(cupcake=serialized), 200)
    elif request.method == "PATCH":
        cupcake.flavor = request.json["flavor"]
        cupcake.size = request.json["size"]
        cupcake.rating = float(request.json["rating"])
        cupcake.image = request.json["image"]
        db.session.commit()
        serialized = [serialize(cupcake)]
        return (jsonify(cupcake=serialized), 200)
    else:
        Cupcake.query.filter_by(id = id).delete() 
        db.session.commit()
        return ({"message":"deleted"}, 200)
