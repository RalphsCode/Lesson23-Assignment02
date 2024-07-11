from models import Cupcake, db
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()
    Cupcake.query.delete()

# Add some cupcakes

vanilla = Cupcake(flavor="vanilla", size="medium", rating=1.0, image = "https://images.unsplash.com/photo-1531112868439-b6b658cfe48a?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGN1cGNha2V8ZW58MHx8MHx8fDA%3D")
chocolate = Cupcake(flavor="chocolate", size="medium", rating=5.0,  image="https://images.unsplash.com/photo-1603532648955-039310d9ed75?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y3VwY2FrZXxlbnwwfHwwfHx8MA%3D%3D")
blueberry = Cupcake(flavor="blueberry", size="medium", rating=3.5, image="https://plus.unsplash.com/premium_photo-1678310877551-396c3953c79e?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y3VwY2FrZXxlbnwwfHwwfHx8MA%3D%3D")
lemon = Cupcake(flavor="lemon", size="large", rating=4.2, image="https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3VwY2FrZXxlbnwwfHwwfHx8MA%3D%3D")

with app.app_context():
    db.session.add_all([vanilla, chocolate, blueberry, lemon])
    db.session.commit()