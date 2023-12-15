#imports
from sqlalchemy.orm import relationship 
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base



Base = declarative_base()


class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column (String(100))
    price = Column (Integer)

    customers = relationship('Customer', secondary='reviews')
    reviews = relationship('Review', back_populates='restaurant')
 
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_name = Column (String(50))
    customer_fullname = Column(String(50))
    star_rating = Column (Integer)

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column (String(50))
    lastname = Column (String(50))

    reviews = relationship('Review', back_populates='customer')
    


       