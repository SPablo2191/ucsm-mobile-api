from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, filters, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentication import token_expire_handler, expires_in
from ..models.student_model import Student
from ..serializers.student_serializer import StudentSerializer,LoginSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ["get", "post", "retrieve", "put", "patch"]
    ordering_fields = ["register_date", "birth_date"]
    filterset_fields = ["identification_document", "email", "status"]
    search_fields = ["identification_document"]
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get("ordering", None)
        if ordering:
            return queryset.order_by(ordering)
        return queryset


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

class StudentLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"success": True, "detail": "Logged out!"}, status=status.HTTP_200_OK)