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

    
    def Restaurant_reviews():
        #returns a collection of all the reviews for the `Restaurant'
        pass

    def Restaurant_customers():
        #returns a collection of all the customers who reviewed the `Restaurant`
        pass
  

class Review(Base):
    __tablename__ = 'reviews'

    def _init_(self,name,price):
        self.id = None
        self.name = name
        self.price = price
    
    def Review_customer():
        # should return the `Customer` instance for this review
        pass
 
    def Review_restaurant():
        # should return the `Restaurant` instance for this review
        pass
 



class Customer(Base):
    __tablename__ = 'customers'

    def _init_(self,firstname,lastname):
        self.id = None
        self.firstname = firstname
        self.lastname = lastname
    def Customer_reviews():
        # should return a collection of all the reviews that the `Customer` has left
        pass
  
    def Customer_restaurants():
        #should return a collection of all the restaurants that the `Customer` has reviewed
        pass
       