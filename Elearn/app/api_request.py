import json
import os
import requests
import configparser
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
config_file_loc = './app/ConfigFile.properties'
course_container = os.environ.get('COURSE_CONTAINER_NAME')
user_container = os.environ.get('USER_CONTAINER_NAME')

def get_user_details(user_id):
    try:
#         config = configparser.ConfigParser()
#         config.read(config_file_loc)
#         url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/getuser/"+str(user_id)
        url = "http://"+user_container+":8080/getuser/"+str(user_id)
        # logger.info("url", url)
        print("URRRL",url)
        response = requests.request(method='GET', url=url)
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result":"Failed"})


def get_users(id):
    try:
#         config = configparser.ConfigParser()
#         config.read(config_file_loc)
#         url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/getusers"
        url = "http://"+user_container+":8080/getusers"
        logger.info("url", url)
        # print("URRRL",url)
        response = requests.request(method='GET', url=url, params={"id":int(id)})
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result":"Failed"})
def get_user_id(name):
    try:
#         config = configparser.ConfigParser()
#         config.read(config_file_loc)
#         url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/getuserid"
        url = "http://"+user_container+":8080/getuserid"
        logger.info("url", url)
        # print("URRRL",url)
        response = requests.request(method='GET', url=url, params={"name":name})
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result":"Failed"})


def check_user(name, pwd):
    try:
#         config = configparser.ConfigParser()
#         config.read(config_file_loc)
#         url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/checkuser"
        url = "http://"+user_container+":8080/checkuser"
        logger.info("url", url)
        # print("URRRL",url)
        response = requests.request(method='POST', url=url, json={"name":name,"password":pwd})
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result":"Failed"})


def delete_user(user_id):
    try:
#         config = configparser.ConfigParser()
#         config.read(config_file_loc)
#         url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/deleteuser/"+str(user_id)
        url = "http://"+user_container+":8080/deleteuser/"+str(user_id)
        logger.info("url", url)
        # print("URRRL",url)
        response = requests.request(method='POST', url=url)
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result":"Failed"})


def add_user(name, password):
    try:
#         config = configparser.ConfigParser()
#         config.read(config_file_loc)
#         url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/adduser"
        url = "http://"+user_container+":8080/adduser"
        logger.info("url", url)
        # print("URRRL", url)
        response = requests.request(method='POST', url=url, json={"name": name, "password": password})
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result": "Failed"})


def add_user_courses(user_id, course_ids):
    logger.info(type(course_ids))
    try:
#         config = configparser.ConfigParser()
#         config.read(config_file_loc)
#         url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') +"/user/"+str(user_id)+"/addcourses"
        url = "http://"+user_container+":8080/user/"+str(user_id)+"/addcourses"
        logger.info("url", url)
       # print("URRRL", url)
        response = requests.request(method='POST', url=url, json={"course_ids":course_ids})
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result": "Failed"})


def get_courses():
    try:
#         config = configparser.ConfigParser()
#         config.read(config_file_loc)
#         url = config.get('courses_request', 'url') + config.get('courses_request', 'port') + "/getcourses"
        url = "http://"+course_container+":8001/getcourses"
        logger.info("url", url)
        # print("URRRL", url)
        response = requests.request(method='GET', url=url)
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result": "Failed"})


def get_course_details(course_id):
    try:
#         config = configparser.ConfigParser()
#         config.read(config_file_loc)
#         url = config.get('courses_request', 'url') + config.get('courses_request', 'port') + "/getcourses/"+str(course_id)
        url = "http://"+course_container+":8001/getcourses/"+str(course_id)
        logger.info("url", url)
        # print("URRRL", url)
        response = requests.request(method='GET', url=url)
        return response.json()
    except Exception as e:
        logger.info(e)
    return json.dumps({"result": "Failed"})

def get_bulk_course_details(course_ids):
    try:
#         config = configparser.ConfigParser()
#         config.read(config_file_loc)
#         url = config.get('courses_request', 'url') + config.get('courses_request', 'port') + "/getcourseslist/"
        url = "http://"+course_container+":8001/getcourseslist/"
        logger.info("url", url)
        # print("URRRL", url)
        response = requests.request(method='GET', url=url, json={"ids": course_ids})
        logger.info(response)
        print(response)
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result": "Failed"})


def add_courses(description,title,duration,author):
    try:
#         config = configparser.ConfigParser()
#         config.read(config_file_loc)
#         url = config.get('courses_request', 'url') + config.get('courses_request', 'port') + "/addcourses/"
        url = "http://"+course_container+":8001/addcourses/"
        logger.info("url", url)
        # print("URRRL", url)
        response = requests.request(method='POST', url=url, json={"description":description,"duration":duration,"title":title,"author":author})
        print(response)
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result": "Failed"})
