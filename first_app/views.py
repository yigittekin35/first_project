from django.shortcuts import render
# from django.http import HttpResponse
from first_app.models import User, Topic, AccessRecord, WebPage
from . import forms
from first_app.forms import NewUser

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    # my_dict = {'insert_me': 'Hello I am from views.py'}
    context_dict = {'text': 'Hello World', 'number': 100}
    return render(request, 'first_app/index.html', context = context_dict)

def help(request):
    help_dict = {'insert_me': 'Hello I am from views.py'}
    return render(request, 'first_app/help.html', context = help_dict)

def users(request):
    # user_list = User.objects.order_by('first_name')
    # user_dict = {'user_records': user_list}
    # return render(request, 'first_app/users.html', context = user_dict)
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('Form is invalid')
    return render(request, 'first_app/users.html', {'form': form})

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('Validation success!')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form': form})

def other(request):
    return render(request, 'first_app/other.html')

def relative(request):
    return render(request, 'first_app/relative_url_templates.html')
