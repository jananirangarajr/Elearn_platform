import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

# Application Default credentials are automatically created.

class Firestore:
    cred = credentials.Certificate("./app/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    course_id = 2

firestore = Firestore()

def get_course_data():
    response = read_course_data()
    return response

def read_course_data():
    users_ref = firestore.db.collection(u'Courses')
    docs = users_ref.stream()
    course_list = []
    for doc in docs:
        data = doc.to_dict()
        data.update({"id": doc.id})
        course_list.append(data)
    # print(course_list)
    return course_list

def get_course(course_id):
    response = get_course_data()
    for course in response:
        if course.get("id") == str(course_id):
            return course
    return {"response":"No Course found"}

def get_course_list(course_ids):
    course_list = []
    response = get_course_data()
    for ids in course_ids:
        for course in response:
            if course.get("id") == str(ids):
                course_list.append(course)
    return course_list

def add_courses(course):
    try:
        doc_ref = firestore.db.collection(u'Courses').document(f'{firestore.course_id}')
        doc_ref.set(
            {
                u'title': f'{course.title}',
                u'description':  f'{course.description}',
                u'duration': f'{course.duration}',
                u'author': f'{course.author}'
            }
        )
        firestore.course_id += 1
        return True
    except:
        return False
