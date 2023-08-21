#!/usr/bin/python3
""" Define State model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """
    State class:
    Define a class State to be linked to db table
    class attribute id that represents a column of an auto-generated,
    unique integer, cant be null and is a primary key
    """
    __tablename__ = "states"

    id = Column(Integer, nullable=False,
                autoincrement=True, unique=True,
                primary_key=True)

    name = Column(String(128), nullable=False)
