#imports 
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base



Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurants'

    def _init_(self,name,price):
        self.id = None
        self.name = name
        self.price = price
    

class Review(Base):
    __tablename__ = 'reviews'

    def _init_(self,name,price):
        self.id = None
        self.name = name
        self.price = price
    pass
class Customer(Base):
    __tablename__ = 'customers'

    def _init_(self,firstname,lastname):
        self.id = None
        self.firstname = firstname
        self.lastname = lastname
    pass