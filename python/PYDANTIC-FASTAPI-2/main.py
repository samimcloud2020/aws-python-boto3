from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Item(BaseModel):
    id: Optional[UUID] = None
    name: str
    price: float

# In a real application, you'd use a database.
# For this example, we'll use a simple in-memory list.
items_db: List[Item] = []

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    """
    Creates a new item and adds it to the database.
    A unique ID is generated for the new item.
    """
    item.id = uuid4()
    items_db.append(item)
    return item

@app.get("/items", response_model=List[Item])
async def get_items():
    """
    Retrieves a list of all items currently in the database.
    """
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: UUID): # Changed type hint to UUID
    """
    Retrieves a single item by its ID.
    Returns a 404 error if the item is not found.
    """
    for item in items_db:
        if item.id == item_id: # Direct comparison with UUID
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: UUID, updated_item: Item):
    """
    Updates an existing item identified by its ID.
    Returns the updated item or a 404 error if not found.
    """
    for index, item in enumerate(items_db):
        if item.id == item_id:
            updated_item.id = item_id  # Ensure the ID remains consistent
            items_db[index] = updated_item
            return items_db[index] # Return the updated item from the list
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: UUID):
    """
    Deletes an item from the database by its ID.
    Returns a success message or a 404 error if not found.
    """
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            return {"message": "Item deleted successfully"} # Corrected spelling
    raise HTTPException(status_code=404, detail="Item not found") # Corrected message consistency
