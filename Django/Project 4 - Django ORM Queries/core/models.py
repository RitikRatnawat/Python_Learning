from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    dept_description = models.TextField()
    employee_count = models.IntegerField(default=1)

    def __str__(self):
        return self.dept_name

    class Meta:
        ordering = ['dept_name']


class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id


class Student(models.Model):
    department = models.ForeignKey(Department, related_name="dept", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="student1_id", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ["student_name"]
        verbose_name = "student"


"""
<model_name>.objects.all().order_by("<attribute_name>") returns queryset of objects in ascending order.
<model_name>.objects.all().order_by("-<attribute_name>") returns queryset of objects in descending order when we put 
                                                        -(minus) sign before the attribute name.
<model_name>.objects.get(<attribute_name> = <value>) returns queryset of objects having attribute values equal to 
                                                        provided value.
<model_name>.objects.filter(<attribute_name> = <value>) returns a filtered queryset of objects and also works with field
                                                        lookups
<model_name>.objects.exclude(<attribute_name> = <value>) returns a queryset of objects in which objects fulfilling the 
                                                        condition will be excluded and also works with field lookups.
                                                        
Some lookups list :
__in
__gt
__lt
__gte
__lte
__exists
__startswith
__endswith
__icontains
__<foreign_key_model>__<lookups> Format to access the foreign key with the lookups

queryset.exists() returns a boolean indicating whether the queryset has objects matching the condition or not.
queryset.distinct(attribute_name) returns a queryset of objects having distinct list of attribute names
queryset.reverse() returns a queryset of objects in reverse order
queryset.values() returns a list of dicts with all the data.
queryset.values_list(list of attribute names) returns a list of dicts of data with only specified attributes.

Aggregated Functions :
<model_name>.objects.aggregate(Avg(<attribute_name>)) returns an average of all the values of the attribute.
<model_name>.objects.aggregate(Max(<attribute_name>)) returns a maximum of all the values of the attribute.
<model_name>.objects.aggregate(Max(<attribute_name>)) returns a minimum of all the values of the attribute.
<model_name>.objects.aggregate(Sum(<attribute_name>)) returns a sum of all the values of the attribute.

Annotated Functions :
<model_name>.objects.values(<attribute_name>).annotate(Count(<attribute_name>)) returns a count of all the values of the
                                                groups grouped by <attribute_name>.
<model_name>.objects.values(<list of attribute_names>).annotate(Count(<attribute_name1>), Avg(<attribute_name2>)) 
                                                performs a count of all the values of the groups grouped by 
                                                <attribute_name1> with average values of <attribute_name2>
"""