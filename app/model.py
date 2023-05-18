from pydantic import BaseModel
from typing import Union
from typing import List
class Course(BaseModel):
    course_ids: List[int]

class User(BaseModel):
    user_id: Union[int, None] = None
    name: Union[str, None] = None
    password: Union[str, None] = None

class Courses(BaseModel):
    title: str
    author: str
    description: Union[str,None] = None
    duration: int
    id: Union[int, None] = None
