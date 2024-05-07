from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, filters, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ucsm_api.views.authentication import token_expire_handler, expires_in
from ucsm_api.views.constants import TagEnum
from ucsm_api.models.student_model import Student
from ucsm_api.serializers.student_serializer import StudentSerializer,LoginSerializer

@extend_schema(tags=[TagEnum.STUDENT.value])
class StudentViewSet(viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ["get","retrieve"]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)


@extend_schema(tags=[TagEnum.AUTH.value])
@permission_classes((AllowAny,))
class StudentLoginAPIView(APIView):
    @extend_schema(
        request=LoginSerializer,
        responses={
            200: {
                "type": "object",
                "properties": {
                    "user": {"$ref": "#/components/schemas/Student"},
                    "expires_in": {"type": "integer"},
                    "token": {"type": "string"},
                },
            },
            400: {"type": "object", "properties": {"error": {"type": "string"}}},
            401: {"type": "object", "properties": {"error": {"type": "string"}}},
        },
    )
    def post(self, request, *args, **kargs):
        if request.method == "POST":
            identification_document = request.data.get("identification_document")
            password = request.data.get("password")
            student = None
            if not (identification_document and password):
                return Response(
                    {
                        "error": "Por favor, proporcione la identificación y la contraseña."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            try:
                student = Student.objects.get(
                    identification_document=identification_document
                )
            except ObjectDoesNotExist:
                return Response(
                    {"error": "Credenciales inválidas"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            student = authenticate(
                identification_document=identification_document, password=password
            )

            if student:
                token, _ = Token.objects.get_or_create(user=student)
                is_expired, token = token_expire_handler(token)
                student_serialized = StudentSerializer(student)
                return Response(
                    {
                        "user": student_serialized.data,
                        "expires_in": expires_in(token),
                        "token": token.key,
                    },
                    status=status.HTTP_200_OK,
                )

            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
@extend_schema(tags=[TagEnum.AUTH.value])
class StudentLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"success": True, "detail": "Logged out!"}, status=status.HTTP_200_OK)