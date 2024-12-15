from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import Item, ItemCreate, ItemResponse  
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items", response_model=list[ItemResponse]) 
async def get_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items

@router.post("/items", response_model=ItemResponse)  
async def add_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item  

@router.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}
