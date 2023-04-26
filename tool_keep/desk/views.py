from django.http import HttpResponse
from django.shortcuts import render

from .models import Tool, User


def index(request):
    main_owner = User.objects.get(username='mainowner')
    print(main_owner.username)
    empty_objects = Tool.objects.filter(owner=main_owner)
    objects = Tool.objects.all()
    users = User.objects.all().exclude(username='mainowner')
    context = {
        'empty_objects': empty_objects,
        'objects': objects,
        'users': users,
        'title': 'Доска оборудования'
    }
    template = 'desk/index.html'
    return render(request, template, context) 

def user_info(request, pk):
    context = {
        
    }
    template = 'desk/index.html'
    return render(request, template, context)
