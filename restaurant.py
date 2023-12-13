from models import Restaurant, Review, Customer
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from models import Base



engine = create_engine('mysql+mysqlconnector://root:P101/0860g/18@localhost/restaurant', echo=True)
with engine.connect() as connection:
    result = connection.execute(text('select "Hi"'))
    print(result.all())
# Create tables in the database
print("CREATING TABLES>>>>>>>")
Base.metadata.create_all(engine)

print("DONE")

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

def insertdata():
    # Use integer values for the 'id' and 'price' fields
    rest = Restaurant(name='ibiza', price=500)
    session.add(rest)
    session.commit()

if __name__ == "__main__":
    insertdata()
