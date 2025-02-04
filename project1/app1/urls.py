from django.urls import path
from .views import *

urlpatterns = [
    path('a/', Base, name='a'),
    path('b/', Sample, name='b'),
    path('username/<str:name>/', StringFun, name='username'),
    path('user_age/<int:age>/', IntegerFun, name='user_age'),
    path('base/', Base, name='base'),
]
