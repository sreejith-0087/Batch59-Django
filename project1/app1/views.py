from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
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

def Template_Extending_Home(request):
    return render(request, '7.Template_Extending(Home).html')

def Template_Extending_Contact(request):
    return render(request, '9.Template_Extending(Contact).html')

def Template_Extending_About(request):
    return render(request, '8.Template_Extending(About).html')

def DataToHtml(request):
    user = Details.objects.all()
    return render(request, '10.DataToHtml.html', {'Users':user})


def UserDetails(request):
    if request.method == 'POST':
        a = UserForm(request.POST)

        if a.is_valid():
            nm = a.cleaned_data['name']
            ag = a.cleaned_data['age']
            sub = a.cleaned_data['subject']
            em = a.cleaned_data['email']

            b = UserModel(Name=nm, Age=ag, Subject=sub, Email=em)
            b.save()

            return HttpResponse('Completed!')
        else:
            return HttpResponse('Failed..')
    return render(request, '11.Forms.html')


def Info(request):
    if request.method == 'POST':
        user = InfoForm(request.POST)

        if user.is_valid():
            nm = user.cleaned_data['name']
            ad = user.cleaned_data['addr']
            em = user.cleaned_data['email']
            ph = user.cleaned_data['phone']

            b = InfoModel(Name=nm, Email=em, Address=ad, Phone=ph)
            b.save()

            return redirect('/profilecard')
        else:
            return HttpResponse('Failed')

    return render(request, '12.Info.html')


def ProfileCard(request):
    profile = InfoModel.objects.all()
    return render(request, '13.Profile.html', {'profile': profile})


def Register(request):
    if request.method == 'POST':
        regform = RegisterForm(request.POST)

        if regform.is_valid():
            nm = regform.cleaned_data['Name']
            phn = regform.cleaned_data['Phone']
            em = regform.cleaned_data['Email']
            pwd = regform.cleaned_data['Password']

            user = RegisterModel(Name=nm, Phone=phn, Email=em, Password=pwd)
            user.save()

            return redirect('/login')
        else:
            return HttpResponse('Invalid')

    return render(request, '14.Register.html')


def Login(request):
    if request.method == 'POST':
        logform = LoginForm(request.POST)

        if logform.is_valid():
            em = logform.cleaned_data['Email']
            pwd = logform.cleaned_data['Password']

            user_details = RegisterModel.objects.all()

            for i in user_details:
                if em==i.Email and pwd==i.Password:
                    return HttpResponse('Login Complete')
                else:
                    return HttpResponse('Invalid Email/Password')
        else:
            return HttpResponse('Invalid Inputs')

    return render(request, '15.Login.html')
