#!/usr/bin/python3
""" User Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ The user class, contains email, password, first and last name """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship(
            'Place', backref='user', cascade='all, delete')
    reviews = relationship(
            'Review', backref='user', cascade='all, delete')

