from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .serializers import StudentSerializer


def get_student(request, id):
    try:
        if id is not None:
            student = Student.objects.get(pk=id)
            st_serializer = StudentSerializer(student)
            return JsonResponse(st_serializer.data)

    except Student.DoesNotExist:
        students = Student.objects.all()
        sts_serializer = StudentSerializer(students, many=True)
        return JsonResponse(sts_serializer.data, safe=False)

@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        data = request.POST
        st_serializer = StudentSerializer(data=data)

        if st_serializer.is_valid():
            st_serializer.save()
            return JsonResponse({"messages": "Student added successfully"})

        return JsonResponse(st_serializer.errors, safe=False)