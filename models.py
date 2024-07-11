from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

###############   MODELS   #############

class Cupcake(db.Model):
    """ Makes Cupcake rows in the cupcakes database """

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    flavor = db.Column(db.Text, nullable=True)

    size = db.Column(db.Text, nullable=True)

    rating = db.Column(db.Float, nullable=True)

    image = db.Column(db.String(255), nullable=False, default= "https://tinyurl.com/demo-cupcake")

