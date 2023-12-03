from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    
    borrowed_books = relationship("Book", secondary="client_books_link")