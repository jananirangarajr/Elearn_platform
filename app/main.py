from fastapi import FastAPI

import firestore
import courses
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

#http://127.0.0.1:8000/docs#

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/getcourses")
async def get_all_courses():
    course_data = firestore.get_course_data()
    if len(course_data) > 0:
        return JSONResponse(content={"result": course_data}, status_code=200)
    return JSONResponse(content={"result": "No Courses available at the moment"}, status_code=201)

@app.get("/getcourses/{course_id}")
async def get_course(course_id: int):
    course_data = firestore.get_course(course_id)
    if len(course_data) > 0:
        return JSONResponse(content={"result": course_data}, status_code=200)
    return JSONResponse(content={"result": "No Course available"}, status_code=201)

@app.get("/getcourseslist/")
async def get_course(course_ids: courses.Course):
    course_data = firestore.get_course_list(course_ids.ids)
    if len(course_data) > 0:
        return JSONResponse(content={"result": course_data}, status_code=200)
    return JSONResponse(content={"result": "No Courses available for the given course ids"}, status_code=201)

@app.post("/addcourses")
async def add_courses(course: courses.Courses):
    result = firestore.add_courses(course)
    if result:
        return JSONResponse(content={"result": "success"}, status_code=200)
    return JSONResponse(content={"result": "failed"}, status_code=201)