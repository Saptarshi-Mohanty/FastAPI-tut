from pydantic import BaseModel

class Item(BaseModel):
    name: str
    descrpition: str|None=None
    price: float
    tax: float|None=None
