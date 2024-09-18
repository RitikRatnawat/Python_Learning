from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    st_serializer = StudentSerializer(student)

    # json_data = JSONRenderer().render(st_serializer.data)

    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(st_serializer.data)


def all_student_details(request):
    students = Student.objects.all()
    sts_serializer = StudentSerializer(students, many=True)

    # json_data = JSONRenderer().render(sts_serializer.data)

    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(sts_serializer.data, safe=False)

