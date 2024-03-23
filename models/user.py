#!/usr/bin/python3
""" User Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """ The user class, contains email, password, first and last name """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place", cascade="all, delete",
                          back_populates="user")
    reviews = relationship("Review", cascade="all, delete",
                           back_populates="user")
