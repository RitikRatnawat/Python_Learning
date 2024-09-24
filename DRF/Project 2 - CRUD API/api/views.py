import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from .models import Student
from .serializers import StudentSerializer


def get_student(request, id):
    try:
        if id is not None:
            student = Student.objects.get(pk=id)
            st_serializer = StudentSerializer(student)
            return JsonResponse(st_serializer.data)

    except Student.DoesNotExist:
        return JsonResponse({"message": "Student not found"})