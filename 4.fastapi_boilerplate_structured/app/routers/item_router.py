from fastapi import APIRouter, HTTPException
from app.models.item import Item, ItemCreate
from app.services.item_service import ItemService

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

item_service = ItemService()

@router.get("/", response_model=list[Item])
async def get_items():
    """모든 아이템 조회"""
    return item_service.get_items()

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """특정 아이템 조회"""
    item = item_service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=Item)
async def create_item(item: ItemCreate):
    """새 아이템 생성"""
    return item_service.create_item(item)

@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemCreate):
    """아이템 수정"""
    updated_item = item_service.update_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/{item_id}")
async def delete_item(item_id: int):
    """아이템 삭제"""
    if not item_service.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
