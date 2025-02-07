from django.urls import path
from .views import *

urlpatterns = [
    path('a/', Base, name='a'),
    path('b/', Sample, name='b'),
    path('username/<str:name>/', StringFun, name='username'),
    path('user_age/<int:age>/', IntegerFun, name='user_age'),
    path('base/', Base, name='base'),
    path('static_file/', Static_file, name='static_file'),
    path('home/', Page_Redirection_Home, name='home'),
    path('about/', Page_Redirection_About, name='about'),
    path('contact/', Page_Redirection_Contact, name='contact'),
    path('', Template_Extending_Home, name='thome'),
    path('tabout/', Template_Extending_About, name='tabout'),
    path('tcontact/', Template_Extending_Contact, name='tcontact'),
]
