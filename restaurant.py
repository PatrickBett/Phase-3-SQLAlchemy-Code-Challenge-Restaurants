from app.models import Restaurant, Review, Customer
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from app.models import Base



engine = create_engine('mysql+mysqlconnector://root:P101/0860g/18@localhost/restaurant', echo=True)
with engine.connect() as connection:
    result = connection.execute(text('select "Hi"'))
    print(result.all())
# Create tables in the database
print("CREATING TABLES>>>>>>")
Base.metadata.create_all(engine)

print("DONE")

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create sample instances
restaurant1 = Restaurant(name="Hilton", price=3)
restaurant2 = Restaurant(name="Heka", price=2)
customer1 = Customer(firstname="Sunshine", lastname="Nganga")
customer2 = Customer(firstname="Anton", lastname="Chupa")

# Add instances to the session
session.add_all([restaurant1, restaurant2, customer1, customer2])

# Commit the changes to the database
session.commit()

# Create sample reviews
review1 = Review(star_rating=4, restaurant_name="Hilton", customer_fullname="Patrick")
review2 = Review(star_rating=5, restaurant_name="Heka", customer_fullname="Brian")
review3 = Review(star_rating=3, restaurant_name="Sunshine", customer_fullname="Daniel")
review4 = Review(star_rating=4, restaurant_name="Highrise", customer_fullname="Michale")

# Add reviews to the session
session.add_all([review1, review2, review3, review4])

# Commit the changes to the database
session.commit()

# Close the session
session.close()
