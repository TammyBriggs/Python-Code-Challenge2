from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from Review import Review

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

# Base class for declarative models
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    reviews = relationship('Review', back_populates='restaurants')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def reviews(self):
        return self.reviews
    
    def customers(self):
        unique_customers = set()
        for review in self.reviews:
            unique_customers.add(review.customer)
        return list(unique_customers)
    
    def average_star_rating(self):
        rating_sum = session.query(func.sum(Review.rating)).filter(Review.restaurant_id == self.id).scalar()
        rating_count = session.query(func.count(Review.rating)).filter(Review.restaurant_id == self.id).scalar()
        if rating_count:
            return rating_sum / rating_count
        else:
            return None