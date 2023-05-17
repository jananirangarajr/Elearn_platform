import json
import requests
import configparser
import logging

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Application Default credentials are automatically created.
class FireStore:
    # cred = credentials.Certificate("./serviceAccountKey.json")
    cred = credentials.Certificate("./app/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    user_id = 200

firestore = FireStore()


def read_user_data():
    users_ref = firestore.db.collection(u'User')
    docs = users_ref.stream()

    return docs
    #for doc in docs:
    #   print(f'{doc.id} => {doc.to_dict()}')

def get_user_data():
    response = read_user_data();
    user_list = []
    for docs in response:
        data = docs.to_dict()
        data.update({"user_id": docs.id})
        user_list.append(data)
    logger.info(f'userlist {user_list}')
    return user_list;

def check_authentication(name, password):
    response = get_user_data()
    # logger.info(len(response))
    logger.info("name",name,"password",password)
    try:
        for doc in response:
            #logger.info(type(doc))
            if str(doc.get("name")) == str(name) and str(doc.get("password")) == str(password):
                return True
    except:
        return False;
    return False;

def add_user(name, password):
    try:
        doc_ref = firestore.db.collection(u'User').document(f'{firestore.user_id}')
        doc_ref.set({
            u'name': f'{name}',
            u'password': f'{password}'
        })
        firestore.user_id += 1
        return True
    except:
        return False

def delete_user(user_id):
    try:
        firestore.db.collection(u'User').document(f'{user_id}').delete()
        return True
    except:
        return False

def get_user_details(user_id):
    # logger.info("userid : ",user_id)
    user_id = str(user_id)
    user_data = {}
    try:
        # doc_ref = firestore.db.collection(u'User').document(user_id)
        doc_ref = firestore.db.collection(f'User').document(f'{user_id}')
        doc = doc_ref.get().to_dict()
        logger.info(doc)
        logger.info("Doc",doc.get("name"))
        logger.info("Doc",user_id)
        courses = []
        if "courses" in doc:
            courses = doc.get("courses")
        user_data.update({"name":doc.get("name"),"id": user_id,"courses":courses})
        print(user_data)
        return user_data
    except Exception as e:
        logger.info(e)
        return False

def get_user_enrolled_courses(user_id):
    user_data = get_user_details(user_id)
    return user_data.get("courses")



def enroll_courses(user_id, course_ids):
    try:
        config = configparser.ConfigParser()
        config.read('./app/ConfigFile.properties')
        url = config.get('request','url')+config.get('request','port')+"/getcourseslist"
        # url = 'http://localhost:8001/getcourseslist'
        logger.info("url", url)
        response = requests.request(method='GET',url=url,json={"ids" : course_ids})
        doc_ref = firestore.db.collection(u'User').document(f'{user_id}')
        ref_response = response.json()
        result = json.loads(json.dumps(ref_response.get("result")))
        user_courses = get_user_enrolled_courses(user_id)
        result = user_courses+result
        doc_ref.set(
            {
                u'courses': result
            },
            merge=True
        )
        return True
    except Exception as e:
        logger.info(e)
        return False


def get_user_id(name):
    response = read_user_data()
    try:
        for doc in response:
            #logger.info(type(doc))
            if str(doc.get("name")) == str(name):
                return doc.id
    except:
        return False;
    return False;