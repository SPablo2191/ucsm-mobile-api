from rest_framework import routers
from django.urls import path
from .views.student_view import StudentViewSet,sign_in
from .views.professor_view import ProfessorViewSet

route = routers.SimpleRouter()
route.register("students", StudentViewSet)
route.register("professors",ProfessorViewSet)

urlpatterns = route.urls

urlpatterns += [
    path('login/', sign_in, name='user-login')
]