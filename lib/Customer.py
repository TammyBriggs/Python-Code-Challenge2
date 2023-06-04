from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///customers.db')
Session = sessionmaker(bind=engine)
session = Session()

# Base class for declarative models
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
    
    def full_name(self):
        return f'{self.given_name} {self.family_name}'
    
    @classmethod
    def all(cls):
        return session.query(cls).all()
