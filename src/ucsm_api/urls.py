from rest_framework import routers
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views.student_view import StudentViewSet,StudentLoginAPIView,StudentLogoutAPIView
from .views.professor_view import ProfessorViewSet

route = routers.SimpleRouter()
route.register("students", StudentViewSet)
route.register("professors",ProfessorViewSet)

urlpatterns = route.urls

urlpatterns += [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('login/', StudentLoginAPIView.as_view(), name='user-login'),
    path('logout/', StudentLogoutAPIView.as_view(), name='user-logout')
]