from sqlalchemy import Column, Integer, String
from .database import Base
from pydantic import BaseModel

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class ItemCreate(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True 
class ItemResponse(ItemCreate):
    id: int
