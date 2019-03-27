import sys, os
import datetime
from time import gmtime, strftime
from sqlalchemy import Column, ForeignKey, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'

    name = Column(String(250), nullable=False, primary_key=True)
    done = Column(Boolean, default=False)
    # time = Column(DateTime, default=datetime.datetime.now)
    time = Column(String(250), default=strftime("%a, %d %b %Y %H:%M:%S", gmtime()))


engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)
