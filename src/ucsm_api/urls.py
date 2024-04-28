from rest_framework import routers
from django.urls import path
from .views.student_view import StudentViewSet,user_login

route = routers.SimpleRouter()
route.register("students", StudentViewSet)

urlpatterns = route.urls

urlpatterns += [
    path('login/', user_login, name='user-login')
]