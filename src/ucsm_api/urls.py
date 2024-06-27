from rest_framework import routers
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from ucsm_api.views.student_view import StudentViewSet,StudentLoginAPIView,StudentLogoutAPIView
from ucsm_api.views.semester_view import SemesterViewSet 
from ucsm_api.views.event_view import EventViewSet
from ucsm_api.views.enrollment_view import EnrollmentViewSet
from ucsm_api.views.subject_registration_view import SubjectRegistrationViewSet
from ucsm_api.views.debt_view import DebtViewSet
from ucsm_api.utils import EndpointEnum

route = routers.SimpleRouter()
route.register(EndpointEnum.STUDENT, StudentViewSet)
route.register(EndpointEnum.SEMESTER,SemesterViewSet)
route.register(EndpointEnum.EVENT,EventViewSet)
route.register(EndpointEnum.ENROLLMENT,EnrollmentViewSet)
route.register(EndpointEnum.SUBJECT_REGISTRATION,SubjectRegistrationViewSet)
route.register(EndpointEnum.DEBT,DebtViewSet)
urlpatterns = route.urls

urlpatterns += [
    path(f'{EndpointEnum.SCHEMA}', SpectacularAPIView.as_view(), name='schema'),
    path(f'{EndpointEnum.DOCS}', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(f'{EndpointEnum.LOGIN}', StudentLoginAPIView.as_view(), name='user-login'),
    path(f'{EndpointEnum.LOGOUT}', StudentLogoutAPIView.as_view(), name='user-logout')
]