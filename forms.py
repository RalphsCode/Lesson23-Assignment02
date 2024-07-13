from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired

class AddCupcake(FlaskForm):
    flavor = StringField("Flavor", validators=[InputRequired()])
    size = StringField("Size", validators=[InputRequired()])
    rating = FloatField("Rating (0.0 - 5.0)", validators=[InputRequired()])
    image = StringField("URL for Cupcake image", validators=[InputRequired()])