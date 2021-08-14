from app import db
from models import Pet

db.drop_all()
db.create_all()

test_pet = Pet(name="Stacy", species="serpent")

db.session.add(test_pet)
db.session.commit()

pet1 = Pet(name="Tommy", species="cat", photo_url="https://urbananimalveterinary.com/wp-content/uploads/2019/10/small-kitten-1.jpg", age=5, notes="Spectacular Cat. He really knows how to have fun!", avaliable=False)
pet2 = Pet(name="Steve", species="Porcupine", photo_url="https://pngimg.com/uploads/hedgehog/hedgehog_PNG6.png", age=1, notes="New Porcupine! So cute!", avaliable=True)
pet3 = Pet(name="Leo", species="Leopard", photo_url="https://e7.pngegg.com/pngimages/607/542/png-clipart-leopard-animal-leopard.png", age=7, notes="He once bit his owner's arm off. Not as cute as you would think...", avaliable=True)

db.session.add_all([pet1, pet2, pet3])
db.session.commit()