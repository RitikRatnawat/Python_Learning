"""Views for the Core App"""

from django.shortcuts import render

# Create your views here.

def index(request):
    """Index view for the Core App"""

    peoples = [
        {'name': 'Paul Groves', 'age': 34},
        {'name': 'Denis B', 'age': 12},
        {'name': 'Gary Learner', 'age': 30},
        {'name': 'Paul Furr', 'age': 17},
        {'name': 'Denis I', 'age': 44}
    ]

    vegetables = ["Pumpkin", "Tomato", "Peas", "Ladyfinger", "Potato", "Cabbage"]

    return render(request, 'index.html', context={'peoples': peoples, 'vegetables':  vegetables, 'page': 'Index'})


def contact(request):
    """Contact view of the Core App"""

    return render(request, "contact.html", context={'page': 'Contact'})


def about(request):
    """About view of the Core App"""

    return render(request, "about.html", context={'page': 'About'})
