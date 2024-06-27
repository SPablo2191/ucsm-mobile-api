from enum import Enum,StrEnum

class EndpointEnum(StrEnum):
    DOCS = 'docs'
    LOGOUT = 'logout'
    LOGIN = 'login'
    SEMESTER = 'semesters'
    BUILDING = 'buildings'
    STUDENT = 'students'
    PROFESSOR = 'professors'
    EVENT = 'events'
    PLAN = 'plans'
    SCHEMA = 'schema'
    ACADEMIC_PROGRAM = 'academic-programs'
    ENROLLMENT = 'enrollments'
    SUBJECT_REGISTRATION = 'subject-registrations'
    DEBT = "debts"