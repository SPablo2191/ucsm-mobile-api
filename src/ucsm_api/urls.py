from rest_framework import routers
from django.urls import path
from .views.student_view import StudentViewSet,sign_in

route = routers.SimpleRouter()
route.register("students", StudentViewSet)

urlpatterns = route.urls

urlpatterns += [
    path('login/', sign_in, name='user-login')
]