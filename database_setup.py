import sys, os
import datetime
from sqlalchemy import Column, ForeignKey, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'

    name = Column(String(250), nullable=False, primary_key=True)
    done = Column(Boolean, default=False)
    time = Column(DateTime, default=datetime.datetime.now)


engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)
