import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

#Database
engine = create_engine('sqlite:////home/conradfay/Projects/demo/demo.db', echo=True)
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
        
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)

#User Add
#ed_user = User('ed', 'Ed Jones', 'password')
#session.add(ed_user)

#session.add_all([
#    User('wendy', 'Wendy Williams', 'foobar'),
#    User('mary', 'Mary Contrary', 'xxg527'),
#    User('fred', 'Fred Flinstone', 'blah'),
#    User('conradfay', 'Conrad Fay', 'password')])

#session.commit()