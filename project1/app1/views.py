from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Base(request):
    return HttpResponse('Hello world')

def Sample(request):
    return HttpResponse('Good Morning!')

def StringFun(request, name):
    return HttpResponse(f'Name is {name}')

def IntegerFun(request, age):
    return HttpResponse(f'Age is {age}')

def Base(request):
    return render(request, '1.Base.html')

def Static_file(request):
    return render(request, '2.Static_file.html')

def Page_Redirection_Home(request):
    return render(request, '3.Page_Redirection(Home).html')

def Page_Redirection_About(request):
    return render(request, '4.Page_Redirection(About).html')

def Page_Redirection_Contact(request):
    return render(request, '5.Page_Redirection(Contact).html')

