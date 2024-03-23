#!/usr/bin/python3
"""Defines the State class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """
    State class
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City",  backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """Get a list of all related City objects."""
            my_list = []
            for item in list(models.storage.all(City).values()):
                if item.state_id == self.id:
                    my_list.append(item)
            return my_list
