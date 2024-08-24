from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UserForm, StudentForm


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