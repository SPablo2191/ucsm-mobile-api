from rest_framework import routers
from .views.student_view import StudentViewSet

route = routers.SimpleRouter()
route.register("students", StudentViewSet)
urlpatterns = route.urls
