from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Table to hold all users
class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    
# Table to hold all authors, used to categorize books
class Author(Base):
    __tablename__ = 'author'
        
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    
# Table to hold books categorize by author
class Books(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    picture = Column(String(250))
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship(Author)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    
engine = create_engine('sqlite:///restaurantmenuwithusers.db')

Base.metadata.create_all(engine)