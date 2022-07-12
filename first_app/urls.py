from django.conf.urls import url
from first_app import views

urlpatterns = [
 url('index', views.index, name = 'index'),
 url('help', views.help, name = 'help'),
 url('users', views.users, name = 'users'),
 url('formpage', views.form_name_view, name = 'form_page'),
]
