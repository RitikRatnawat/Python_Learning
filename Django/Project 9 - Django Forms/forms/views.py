from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UserForm, StudentForm, DynamicForm


# Create your views here.
def user_form(request):
    if request.method == 'POST':
        print(request.POST)

    context = {'user_form': UserForm()}
    return render(request, 'forms/user_form.html', context)


def student_form(request):

    form = StudentForm()

    if request.method == 'POST':
        valid_form = StudentForm(request.POST)
        if valid_form.is_valid():
            valid_form.save()

    context = {'student_form': form}
    return render(request, 'forms/student_form.html', context)


class StudentFormView(FormView):
    template_name = 'forms/student_form_view.html'
    form_class = StudentForm
    success_url = "/forms/student_form_view"

    def form_valid(self, form):
        student = form.save()
        print(student)

        return super(StudentFormView, self).form_valid(form)


def dynamic_form(request):
    form1 = DynamicForm(auto_id="some_%s") # These format create id of a form field with specified prefix or suffix.
    form2 = DynamicForm(auto_id=True) # These format create id of a form field with same as name of the field.
    form3 = DynamicForm(auto_id=False) # These format removes id from the form field.
    form4 = DynamicForm(auto_id="forms") # These format also act same as True format as value is True.
    form5 = DynamicForm(label_suffix=' -> ') # Configure labels for the form fields.
    form6 = DynamicForm(initial={"first_name": "Paul",
                                 "last_name": "Groves",
                                 "email": "groves.paul@example.com"}) # Configure initial values for the form fields.
    form7 = DynamicForm() # Ordering form fields
    form7.order_fields(["email", "first_name", "last_name"])
    form8 = DynamicForm(label_suffix=" -> ")

    if request.method == 'POST':
        print(request.POST)

    context = {"form1": form1, "form2": form2, "form3": form3,
               "form4": form4, "form5": form5, "form6": form6,
               "form7": form7, "form8": form8}
    return render(request, 'forms/dynamic_form.html', context=context)