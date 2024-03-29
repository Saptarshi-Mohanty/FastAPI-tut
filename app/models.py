from pydantic import BaseModel, Field, HttpUrl

class Image(BaseModel):
    name: str
    description: str
    url : HttpUrl

class Item(BaseModel):
    name: str
    descrpition: str|None=None
    price: float
    tax: float|None=None
    image: Image

class User(BaseModel):
    username_first: str| None = Field(None, title="First Name", max_length=20)
    username_last: str| None = Field(..., title="Last Name", max_length=25)
