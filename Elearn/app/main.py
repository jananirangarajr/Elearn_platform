from fastapi import FastAPI
import api_request
import model
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello Users"}


@app.get("/elearn/getuser/{user_id}")
async def get_user(user_id: int):
    return api_request.get_user_details(user_id)

@app.get("/elearn/getusers")
async def get_user(id : int):
    return api_request.get_users(id)

@app.get("/elearn/getuserid")
async def get_user(name : str):
    return api_request.get_user_id(name)

@app.post("/elearn/checkuser")
async def find_user(user : model.User):
    return api_request.check_user(user.name, user.password)
@app.post("/elearn/deleteuser/{user_id}")
async def delete_user(user_id : int):
    return api_request.delete_user(user_id)

@app.post("/elearn/adduser")
async def add_user(user : model.User):
    return api_request.add_user(user.name, user.password)

@app.post("/elearn/user/{user_id}/addcourses")
async def add_user_courses(user_id : int, course_id: model.Course):
    return api_request.add_user_courses(user_id, course_id.course_ids)

@app.get("/elearn/getcourses")
async def get_all_courses():
    return api_request.get_courses()

@app.get("/elearn/getcourses/{course_id}")
async def get_course(course_id: int):
    return api_request.get_course_details(course_id)

@app.get("/elearn/getcourseslist")
async def get_courses_list(ids: model.Course):
    return api_request.get_bulk_course_details(ids.course_ids)

@app.post("/elearn/addcourses")
async def add_courses(course: model.Courses):
    return api_request.add_courses(course.description, course.title, course.duration, course.author)

