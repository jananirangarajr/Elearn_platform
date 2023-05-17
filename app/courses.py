from pydantic import BaseModel, Field
from typing import Union
from typing import List

class Course(BaseModel):
    ids : List[int]

class Courses(BaseModel):
    title: str
    author: str
    description: Union[str,None] = None
    duration: int
    id: Union[int, None] = None
