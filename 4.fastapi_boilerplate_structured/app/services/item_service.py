from app.models.item import Item, ItemCreate

class ItemService:
    def __init__(self):
        self.items = []
        self.counter = 0

    def get_items(self) -> list[Item]:
        return self.items

    def get_item(self, item_id: int) -> Item | None:
        return next((item for item in self.items if item.id == item_id), None)

    def create_item(self, item: ItemCreate) -> Item:
        self.counter += 1
        new_item = Item(
            id=self.counter,
            name=item.name,
            description=item.description
        )
        self.items.append(new_item)
        return new_item

    def update_item(self, item_id: int, item: ItemCreate) -> Item | None:
        existing_item = self.get_item(item_id)
        if existing_item:
            existing_item.name = item.name
            existing_item.description = item.description
            return existing_item
        return None

    def delete_item(self, item_id: int) -> bool:
        item = self.get_item(item_id)
        if item:
            self.items.remove(item)
            return True
        return False
