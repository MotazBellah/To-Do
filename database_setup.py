import sys. os
from sqlalchemy im import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'

    name = Column(String(250), nullable=False, primary_key=True)
    done = Column(Boolean, default=False)


engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)
