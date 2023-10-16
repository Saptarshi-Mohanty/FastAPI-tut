from pydantic import BaseModel

class Item(BaseModel):
    name: str
    descrpition: str|None=None
    price: float
    tax: float|None=None

class User(BaseModel):
    username_first: str
    username_last: str