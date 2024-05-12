from django.urls import reverse
from rest_framework import status
from rest_framework.test import  force_authenticate

from ucsm_api.views.student_view import StudentViewSet
from test_base_endpoint import BaseTests

class StudentTests(BaseTests):
    def test_get_student(self):
        self.view = StudentViewSet.as_view({'get': 'retrieve'})
        url = reverse('student-detail',args=[{'pk':self.student.pk}])
        request = self.factory.get(url)
        force_authenticate(request, user=self.student, token=self.token)
        response = self.view(request, pk=self.student.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
