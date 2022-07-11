from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me': 'Hello I am from views.py'}
    return render(request, 'first_app/index.html', context = my_dict)

def help(request):
    help_dict = {'insert_me': 'Hello I am from views.py'}
    return render(request, 'first_app/help.html', context = help_dict)
