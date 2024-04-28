from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from ..models.student_model import Student
from ..serializers.student_serializer import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ["get", "post", "retrieve", "put", "patch"]
    ordering_fields = ["register_date","birth_date"]
    filterset_fields = ["identification_document","email","status"]
    search_fields = ["identification_document"]
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get("ordering", None)
        if ordering:
            return queryset.order_by(ordering)
        return queryset
