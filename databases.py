from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def createSession():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session 

def addProduct(name, price, description):
	session = createSession()
	product_object = Product (
		name= name ,
		price=price ,
		description=description)
	session = createSession()
	session.add(product_object)
	session.commit()


def editProduct(id, name): #by id
	session = createSession()
	product_object = session.query(
       Student).filter_by(
       id=id).first()
	product_object.price = price
	product_object.pictureLink = pictureLink
	session.commit()

def deleteProduct(name):
	session = createSession()
	session.query(Product).filter_by(
       id=id).delete()
	session.commit()

def query_all():
	session = createSession()
	products = session.query(
      Product).all()
	return products

def query_by_id(id):
	session = createSession()
	product = session.query(
       Product).filter_by(
       id=id).first()
	return product




