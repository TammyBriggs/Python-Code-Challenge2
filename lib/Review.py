from sqlalchemy import create_engine, Column, Integer, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///reviews.db')
Session = sessionmaker(bind=engine)
session = Session()

# Base class for declarative models
Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    rating = Column(Float)

    customer = relationship('Customer', backref='reviews')
    restaurant = relationship('Restaurant', backref='reviews')

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def rating(self):
        return self.rating
    
    @classmethod
    def all(cls):
        return session.query(cls).all()