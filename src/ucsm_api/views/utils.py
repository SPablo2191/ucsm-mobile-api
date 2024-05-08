from enum import Enum

class TagEnum(str,Enum):
    AUTH = "Auth"
    STUDENT = "Student"
    PROFESSOR = "Professor"
    SEMESTER = "Semester"
    BUILDING = "Building"
    EVENT = "Event"
    PLAN = "Plan"
    SUBJECT_REGISTRATION = "Subject Registration"
    ACADEMIC_PROGRAM = "Academic Program"
    ENROLLMENT = "Enrollment"
    DEBT = "Debt"
