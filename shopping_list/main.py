from fastapi import FastAPI, HTTPException, status

from shopping_list.models import Item

app = FastAPI()

market_list: list[Item] = [
    Item(name='Mock item 01', quantity=5, value=10.5),
    Item(name='Mock item 02', quantity=2, value=11.2),
    Item(name='Mock item 03', quantity=10, value=18.2),
]


@app.get('/items')
async def read_items():
    return market_list


@app.get('/items/{uuid}')
async def read_item_by_id(uuid: str):
    item = next((item for item in market_list if item.id == uuid), None)
    if item:
        return item.model_dump_json()
    raise HTTPException(status_code=404, detail='Item not found')


@app.post('/items', status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    market_list.append(item)
    return {'message': 'Item added successfully', 'item': item.model_dump_json()}


@app.delete('/items/{uuid}')
async def delete_item(uuid: str):
    for index, item in enumerate(market_list):
        if item.id == uuid:
            del market_list[index]
            return {'message': 'Item deleted successfully', 'item': item.model_dump_json()}

    raise HTTPException(status_code=404, detail='Item not found')
