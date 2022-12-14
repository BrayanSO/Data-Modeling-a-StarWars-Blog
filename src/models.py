import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    faw_planets = relationship('fav_planets', backref='user', lazy=True)
    faw_characters = relationship ('fav_planets', backref='user', lazy=True)
    

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    faw_characters = relationship ('fav_planets', backref='user', lazy=True)

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Fav_films(Base):
    __tablename__ = 'fav_films'
    id = Column(Integer, primary_key=True)
    user_id =Column (Integer, ForeignKey('user.id'))
    films_id = Column (Integer, ForeignKey('films.id'))

class Fav_planets(Base):
    __tablename__ = 'fav_planets'
    id = Column(Integer, primary_key=True)
    user_id =Column (Integer, ForeignKey('user.id'))
    planets_id = Column (Integer, ForeignKey('planets.id'))





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
