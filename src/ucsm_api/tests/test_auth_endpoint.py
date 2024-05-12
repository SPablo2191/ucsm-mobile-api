from django.urls import reverse
from rest_framework import status
from rest_framework.test import  force_authenticate

from ucsm_api.views.student_view import StudentLogoutAPIView
from test_base_endpoint import BaseTests

class AuthTests(BaseTests):
    def test_login(self):
        url = reverse("user-login")
        data = {"identification_document": "20232120", "password": "contraseña_123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_incorrect_login(self):
        url = reverse("user-login")
        data = {"identification_document": "20242120", "password": "contraseña_123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout(self):
        self.view = StudentLogoutAPIView.as_view()
        url = reverse("user-logout")
        request = self.factory.post(url)
        force_authenticate(request, user=self.student, token=self.token)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
