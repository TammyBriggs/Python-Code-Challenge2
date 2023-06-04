from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

# Base class for declarative models
Base = declarative_base()

class Restaurant(Base):
    