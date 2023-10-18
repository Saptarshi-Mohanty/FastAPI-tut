from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, time

from food import Food
from models import Item, User

app = FastAPI()

small_db = [{"Protien" : ['Meat', 'Dairy', 'Soya', 'Egg']},
            {"Carbs" : ['Bread', 'Noodles', 'Cheese']},
            {"Vitamins" : ['Fruits', 'Vegetables', 'Dhoop']}]

uuid = "cd43be2f-d103-4863-8546-70d7d8ee7921"

@app.get("/")
async def root():
    return {"message": "hello world"}

@app.post("/")
async def post():
    return {"message": "hello world from post request"}

@app.get("/foods/{foodname}")
async def get_food(foodname: Food):
    if foodname == Food.dairy:
        return "Hope you aint lactose intolorant"
    elif foodname.value == 'fruits':
        return "Enjoy sweet food"
    return "Protien ftw"

# @app.get("/foods")
# async def list_food(start: int=0, stop: int=5):
#     return small_db[start: stop]

@app.get("/item/hidden")
async def hidden_route(hidden_query: str|None = Query(None, include_in_schema=False, alias='hq')):
    if hidden_query:
        return {"Hidden Query": hidden_query}
    return {"Hidden Query": "Not found"}

@app.get("/item/validation/{item_id}")
async def item_validation(q: str|None = Query(None, max_length=10), item_id: int|None = Path(..., title="Path parameter")):
    results = {"item ID": item_id}
    if q:
        results.update({"Query": q})
    return results

@app.get("/item/{item_id}")
async def item_list(item_id: str, q: str|None = None, story: bool = False):
    if q:
        if story:
            return "lorem10"
        else:
            return {"item" : item_id, "query": q}
    return {"item": item_id}

@app.post("/item")
async def get_item(item: Item):
    item_dic = item.model_dump()
    if item.tax:
        item_dic.update({"price after tax": item.price+item.tax})
    return item_dic

@app.get("/item")
async def read_item(q: str|None = Query(None, min_length=3, max_length=10, title='sample fastapi query', description='Sample api call', alias='simple-query')):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# @app.put("/item/{item_id}")
# async def update_item(item: Item|None=None, user: User|None=None, item_id: int = Path(...,ge=0, le=100), q: str|None = None):
#     results = {"Item ID": item_id}
#     if q:
#         results.update({"Query": q})
#     if user:
#         results.update({"User": user})
#     if item:
#         results.update({"Item": item})
#     return results

@app.put("/item/{item_id}")
async def read_items(item_id: UUID, start_time: datetime|None = Body(None)):
    result = {"Item ID": item_id}
    if start_time:
        result.update({"Start Time": start_time})
    return result
