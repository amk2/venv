from sqlalchemy import Column, Integer, String
from database import Base


"""
the __init__() method

Our User class, as defined using the Declarative system, has been provided with a constructor (e.g. __init__() method) which automatically accepts keyword names that match the columns we’ve mapped. We are free to define any explicit __init__() method we prefer on our class, which will override the default method provided by Declarative.

"""

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)
