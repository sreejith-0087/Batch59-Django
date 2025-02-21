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
    path('thome/', Template_Extending_Home, name='thome'),
    path('tabout/', Template_Extending_About, name='tabout'),
    path('tcontact/', Template_Extending_Contact, name='tcontact'),
    path('datatohtml/', DataToHtml, name='datatohtml'),
    path('userdata/', UserDetails, name='userdata'),
    path('userinfo/', Info, name='userinfo'),
    path('profilecard/', ProfileCard, name='profilecard'),
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('home/', Auth_Base, name='home'),
    path('auth_register/', Auth_Register, name='auth_reg'),
    path('auth_login/', Auth_Login, name='auth_login'),
    path('auth_logout/', Auth_Logout, name='auth_logout'),
    path('', FileUpload, name='file_upload'),
    path('display/', Display_Uploaded_File, name='display'),
]

