from pydantic import BaseModel, validator, conint, constr, conlist
from enum import Enum
import datetime

class Level(Enum):
    S_Class = 1
    A_Class = 2
    B_class = 3
    F_Class = 4

class Student(BaseModel):
    name: constr(max_length=10)
    age: conint(ge=18, le=60)
    joined: datetime.date
    level: Level|None=None

    @validator("age")
    def check_age(cls, age):
        if age<10:
            raise ValueError("Age must be greater than 10")
        return age
    
    @validator("level")
    def check_level_wrt_age(cls, level, values):
        if level:
            if level is Level.S_Class and values["age"]<=20:
                raise ValueError("Have to be above 20 to be S class")
        return level
    
class Course(BaseModel):
    title: str
    student: conlist(item_type=Student)|None = []

student_obj = Student(name='Happy', age=22, joined=datetime.date(year=1999, day=10, month=8))

course_obj = Course(title="Math AP")
course_obj.student.append(student_obj)
print(course_obj.model_dump_json)