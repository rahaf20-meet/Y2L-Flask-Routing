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
	session.add(product_object)
	session.commit()
	session.close()


def editProduct(Id, name): #by id
	session = createSession()
	product_object = session.query(
       Student).filter_by(
       Id=Id).first()
	product_object.price = price
	product_object.pictureLink = pictureLink
	session.commit()

def deleteProduct(name):
	session = createSession()
	session.query(Product).filter_by(
       name=name).delete()
	session.commit()

def query_all():
	session = createSession()
	products = session.query(
      Product).all()
	session.close()
	return products

def query_by_id(Id):
	session = createSession()
	product = session.query(
       Product).filter_by(
       Id=Id).first()
	return product



# addProduct("wafers", 7, "made with love")
#deleteProduct("chocolate donuts")
print(len(query_all())) 
