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
    