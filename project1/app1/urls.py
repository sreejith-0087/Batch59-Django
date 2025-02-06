from django.urls import path
from .views import *

urlpatterns = [
    path('a/', Base, name='a'),
    path('b/', Sample, name='b'),
    path('username/<str:name>/', StringFun, name='username'),
    path('user_age/<int:age>/', IntegerFun, name='user_age'),
    path('base/', Base, name='base'),
    path('static_file/', Static_file, name='static_file'),
    path('', Page_Redirection_Home, name='home'),
    path('about/', Page_Redirection_About, name='about'),
    path('contact/', Page_Redirection_Contact, name='contact'),
]
