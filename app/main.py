from fastapi import FastAPI, Query
from pydantic import BaseModel

from food import Food
from models import Item

app = FastAPI()

small_db = [{"Protien" : ['Meat', 'Dairy', 'Soya', 'Egg']},
            {"Carbs" : ['Bread', 'Noodles', 'Cheese']},
            {"Vitamins" : ['Fruits', 'Vegetables', 'Dhoop']}]

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
async def read_item(q: str|None = Query(None, min_length=3, max_length=10, title='sample fastapi query', description='Sample api call')):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
