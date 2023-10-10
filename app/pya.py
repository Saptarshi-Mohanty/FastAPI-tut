from pydantic import BaseModel, field_validator
from enum import Enum
import datetime

class Level(Enum):
    S_Class = 1
    A_Class = 2
    B_class = 3
    F_Class = 4

class Student(BaseModel):
    name: str
    age: int
    joined: datetime.date
    level: Level

    @field_validator("age")
    def check_age(cls, age):
        if age<10:
            raise ValueError("Age must be greater than 10")
        return age
    
    @field_validator("level")
    def check_level_wrt_age(cls, level, values):
        if level is Level.S_Class and values["age"]<=20:
            raise ValueError("Have to be above 20 to be S class")
        return level, values

student_obj = Student(name='Happy', age=1, joined=datetime.date(year=1999, day=10, month=8), level=1)

print(student_obj)