import io
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer


def get_students(request):
    try:
        students = Student.objects.all()
        sts_serializer = StudentSerializer(students, many=True)
        return JsonResponse(sts_serializer.data, safe=False)

    except Student.DoesNotExist:
        return JsonResponse({"message": "No Students exists"})


@csrf_exempt
def cud_student(request, id):

    if request.method == 'GET':
        try:
            if id is not None:
                student = Student.objects.get(pk=id)
                st_serializer = StudentSerializer(student)
                return JsonResponse(st_serializer.data)

        except Student.DoesNotExist:
            return JsonResponse({"message": "Student does not exist"})

    if request.method == 'PUT':
        data = request.body
        stream = io.BytesIO(data)
        parsed_data = JSONParser().parse(stream)

        try:
            student = Student.objects.get(id=id)
            st_serializer = StudentSerializer(student, data=parsed_data, partial=True)

            if st_serializer.is_valid():
                st_serializer.save()

            response = {
                "message": "Data updated successfully",
                "updated_data": st_serializer.data
            }

            return JsonResponse(response)

        except Student.DoesNotExist:
            return JsonResponse({"message": "Student does not exist"})

    if request.method == 'DELETE':

        try:
            student = Student.objects.get(id=id)
            student.delete()

            response = {
                "message": "Data deleted successfully",
            }

            return JsonResponse(response)

        except Student.DoesNotExist:
            return JsonResponse({"message": "Student does not exist"})


@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        data = request.POST
        st_serializer = StudentSerializer(data=data)

        if st_serializer.is_valid():
            st_serializer.save()
            return JsonResponse({"messages": "Student added successfully"})

        return JsonResponse(st_serializer.errors, safe=False)