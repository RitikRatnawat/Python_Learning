import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)

        data = JSONParser().parse(stream)

        st_serializer = StudentSerializer(data=data)
        if st_serializer.is_valid():
            st_serializer.save()
            response = {"message": "Student Added Successfully"}
            response_json = JSONRenderer().render(response)
            return HttpResponse(response_json, content_type="application/json")

        return JsonResponse(st_serializer.errors)



