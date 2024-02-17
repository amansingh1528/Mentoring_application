from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

# Replace 'sqlite:///data/mentorship.db' with your actual database URI
engine = create_engine('sqlite:////Users/mac/IdeaProjects/Google/data/mentorship.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
