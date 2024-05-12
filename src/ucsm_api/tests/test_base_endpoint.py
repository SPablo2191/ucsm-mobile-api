from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.views import APIView
import uuid

from ucsm_api.models.student_model import Student



class BaseTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.student = Student.objects.create_user(
            id = uuid.uuid4(),
            identification_document="20232120",
            email="student@example.com",
            password="contraseña_123",
            first_name="John",
            last_name="Doe",
        )
        self.view = APIView.as_view()
        self.token = Token.objects.get_or_create(user=self.student)[0].key
