from enum import Enum

class EndpointEnum(str,Enum):
    DOCS = 'docs'
    LOGOUT = 'logout'
    LOGIN = 'login'
    SEMESTER = 'semesters'
    BUILDING = 'buildings'
    STUDENT = 'students'
    PROFESSOR = 'professors'
    SCHEMA = 'schema'