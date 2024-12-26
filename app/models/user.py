from app.backend.db import *

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firtsname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique = True, index = True)
    tasks = relationship('Task', back_populates='tasks')

print(CreateTable(User.__table__))
