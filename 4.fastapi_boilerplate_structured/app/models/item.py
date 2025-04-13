from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

class ItemCreate(BaseModel):
    name: str
    description: str | None = None
