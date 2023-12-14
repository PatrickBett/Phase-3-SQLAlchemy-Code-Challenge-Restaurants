#imports 
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base



Base = declarative_base()


class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column (String(100))
    price = Column (Integer)
 
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_name = Column (String(50))
    customer_fullname = Column(String(50))
    star_rating = Column (Integer)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column (String(50))
    lastname = Column (String(50))


       