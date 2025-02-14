from django.shortcuts import render
from django.http import HttpResponse
from .models import Details, UserModel
from .forms import UserForm
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
