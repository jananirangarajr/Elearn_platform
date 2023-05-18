import json

import requests
import configparser
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
config_file_loc = './app/ConfigFile.properties'

def get_user_details(user_id):
    try:
        config = configparser.ConfigParser()
        config.read(config_file_loc)
        url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/getuser/"+str(user_id)
        # logger.info("url", url)
        print("URRRL",url)
        response = requests.request(method='GET', url=url)
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result":"Failed"})


def get_users(id):
    try:
        config = configparser.ConfigParser()
        config.read(config_file_loc)
        url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/getusers"
        logger.info("url", url)
        # print("URRRL",url)
        response = requests.request(method='GET', url=url, params={"id":int(id)})
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result":"Failed"})
def get_user_id(name):
    try:
        config = configparser.ConfigParser()
        config.read(config_file_loc)
        url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/getuserid"
        logger.info("url", url)
        # print("URRRL",url)
        response = requests.request(method='GET', url=url, params={"name":name})
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result":"Failed"})


def check_user(name, pwd):
    try:
        config = configparser.ConfigParser()
        config.read(config_file_loc)
        url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/checkuser"
        logger.info("url", url)
        # print("URRRL",url)
        response = requests.request(method='POST', url=url, json={"name":name,"password":pwd})
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result":"Failed"})


def delete_user(user_id):
    try:
        config = configparser.ConfigParser()
        config.read(config_file_loc)
        url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/deleteuser/"+str(user_id)
        logger.info("url", url)
        # print("URRRL",url)
        response = requests.request(method='POST', url=url)
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result":"Failed"})


def add_user(name, password):
    try:
        config = configparser.ConfigParser()
        config.read(config_file_loc)
        url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') + "/adduser"
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
        config = configparser.ConfigParser()
        config.read(config_file_loc)
        url = config.get('user_request', 'user_url') + config.get('user_request', 'user_port') +"/user/"+str(user_id)+"/addcourses"
        logger.info("url", url)
       # print("URRRL", url)
        response = requests.request(method='POST', url=url, json={"course_ids":course_ids})
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result": "Failed"})


def get_courses():
    try:
        config = configparser.ConfigParser()
        config.read(config_file_loc)
        url = config.get('courses_request', 'url') + config.get('courses_request', 'port') + "/getcourses"
        logger.info("url", url)
        # print("URRRL", url)
        response = requests.request(method='GET', url=url)
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result": "Failed"})


def get_course_details(course_id):
    try:
        config = configparser.ConfigParser()
        config.read(config_file_loc)
        url = config.get('courses_request', 'url') + config.get('courses_request', 'port') + "/getcourses/"+str(course_id)
        logger.info("url", url)
        # print("URRRL", url)
        response = requests.request(method='GET', url=url)
        return response.json()
    except Exception as e:
        logger.info(e)
  return json.dumps({"result": "Failed"})

def get_bulk_course_details(course_ids):
    try:
        config = configparser.ConfigParser()
        config.read(config_file_loc)
        url = config.get('courses_request', 'url') + config.get('courses_request', 'port') + "/getcourseslist/"
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
        config = configparser.ConfigParser()
        config.read(config_file_loc)
        url = config.get('courses_request', 'url') + config.get('courses_request', 'port') + "/addcourses/"
        logger.info("url", url)
        # print("URRRL", url)
        response = requests.request(method='POST', url=url, json={"description":description,"duration":duration,"title":title,"author":author})
        print(response)
        return response.json()
    except Exception as e:
        logger.info(e)
        return json.dumps({"result": "Failed"})
