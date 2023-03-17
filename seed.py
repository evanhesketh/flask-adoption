from models import db, Pet
import app


#refresh tables
db.drop_all()
db.create_all()


p = Pet(name="bubbles",species="dog",photo_url="",age="baby", notes='So cute!')

p2 = Pet(name="lemon",species="cat",photo_url="",age="young", notes='')

db.session.add(p)
db.session.add(p2)

db.session.commit()