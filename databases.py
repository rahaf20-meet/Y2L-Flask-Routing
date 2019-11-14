from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def addProduct(price, pictureLink, description):
	product_object = Product (
		price=price ,
		pictureLink=pictureLink ,
		description=description)
	session.add(product_object)
	session.commit()

def editProduct(id, price, pictureLink, description): #by id
	product_object = session.query(
       Student).filter_by(
       id=id).first()
	product_object.price = price
	product_object.pictureLink = pictureLink
	product_object.description = description
	session.commit()

def deleteProduct(id, price, pictureLink, description):
   session.query(Product).filter_by(
       id=id).delete()
   session.commit()

def query_all():
   products = session.query(
      Product).all()
   return products

def query_by_id(id):
   product = session.query(
       Product).filter_by(
       id=id).first()
   return product




