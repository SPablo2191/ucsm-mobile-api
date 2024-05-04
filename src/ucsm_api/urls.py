from rest_framework import routers
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views.student_view import StudentViewSet,StudentLoginAPIView,StudentLogoutAPIView
from .views.professor_view import ProfessorViewSet
from .views.building_view import BuildingViewSet
from .views.semester_view import SemesterViewSet 
from .constants import EndpointEnum

route = routers.SimpleRouter()
route.register(EndpointEnum.STUDENT, StudentViewSet)
route.register(EndpointEnum.PROFESSOR,ProfessorViewSet)
route.register(EndpointEnum.BUILDING,BuildingViewSet)
route.register(EndpointEnum.SEMESTER,SemesterViewSet)
urlpatterns = route.urls

urlpatterns += [
    path(f'{EndpointEnum.SCHEMA}/', SpectacularAPIView.as_view(), name='schema'),
    path(f'{EndpointEnum.DOCS}/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(f'{EndpointEnum.LOGIN}/', StudentLoginAPIView.as_view(), name='user-login'),
    path(f'{EndpointEnum.LOGOUT}/', StudentLogoutAPIView.as_view(), name='user-logout')
]