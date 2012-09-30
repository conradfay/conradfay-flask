import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

#Database
engine = create_engine('sqlite:////home/conradfay/database/conradfay-flask.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    password = Column(String)
    
    
    def __init__(self, username, firstname, lastname, password):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.firstname, self.lastname, self.password)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
#User Add
#ed_user = User('ed', 'Ed Jones', 'password')
#session.add(ed_user)

#session.add_all([
#    User('wendy', 'Wendy Williams', 'foobar'),
#    User('mary', 'Mary Contrary', 'xxg527'),
#    User('fred', 'Fred Flinstone', 'blah'),
#    User('conradfay', 'Conrad Fay', 'password')])

#session.commit()