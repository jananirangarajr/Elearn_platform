import json

from fastapi import FastAPI

import firestore
import user
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


# http://127.0.0.1:8000/docs#

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/getuser/{user_id}")
async def get_user_details(user_id : str):
    user_data = firestore.get_user_details(user_id)
    if user_data != False:
        return JSONResponse(content={"result": user_data}, status_code=200)
    else:
        return JSONResponse(content={"result": "Failed"}, status_code=201)


@app.get("/getusers")
async def get_user(id : int):
    if id == 100:
        user_data = firestore.get_user_data()
        return JSONResponse(content={"result": user_data}, status_code=200)
    else:
        return JSONResponse(content={"result": "You are not administrator"}, status_code=201)

@app.get("/getuserid")
async def get_user(name : str):
    user_id = firestore.get_user_id(name)
    if user_id == False:
        return JSONResponse(content={"result": "You are not a valid user"}, status_code=201)
    return JSONResponse(content={"result": user_id}, status_code=200)

@app.post("/checkuser")
async def find_user(user : user.User):
    result = firestore.check_authentication(user.name,user.password)
    if result: 
        return JSONResponse(content={"result": result}, status_code=200)
    return JSONResponse(content={"result": "You are not authorised user"}, status_code=201)

@app.post("/deleteuser/{user_id}")
async def delete_user(user_id : int):
    result = firestore.delete_user(user_id)
    if result:
        return JSONResponse(content={"result":"success"}, status_code=200)
    return JSONResponse(content={"response": "failed"}, status_code=201)

@app.post("/adduser")
async def add_user(user : user.User):
    result = firestore.add_user(user.name,user.password)
    if result:
        return JSONResponse(content={"response":"success"}, status_code=200)
    return JSONResponse(content={"response": "failed"}, status_code=201)


@app.post("/user/{user_id}/addcourses")
async def add_courses(user_id : int, course_id: user.Course):
    result = firestore.enroll_courses(user_id,course_id.course_ids)
    if result:
        return JSONResponse(content={"response":"success"}, status_code=200)
    return JSONResponse(content={"response": "failed"}, status_code=201)

