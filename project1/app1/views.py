from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMessage
from .models import *
from .forms import *

# Class based views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


def Auth_Base(request):
    return render(request, '16.Auth_Base.html')


def Auth_Register(request):
    if request.method == 'POST':
        f_name = request.POST['Name']
        email = request.POST['Email']
        password = request.POST['Password']
        re_password = request.POST['Re-Password']

        if password == re_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exist!')
            else:
                user = User.objects.create_user(username=email, first_name=f_name, email=email, password=password)
                user.save()
                messages.success(request, 'Registration Complate')
                return redirect('/auth_login')
        else:
            messages.error(request, 'Password does not match')

    return render(request, '17.Auth_Register.html')


def Auth_Login(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['Password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Complete')
            return redirect('/')
        else:
            messages.error(request, 'Invalid')
    return render(request, '18.Auth_Login.html')


def Auth_Logout(request):
    logout(request)
    return redirect('/')


def FileUpload(request):
    if request.method == 'POST':
        fileup = FileForm(request.POST, request.FILES)

        if fileup.is_valid():
            nme = fileup.cleaned_data['File_Name']
            file = fileup.cleaned_data['File']

            FileModel(FileName=nme, File=file).save()

            return redirect('/display')
        else:
            return HttpResponse('Failed')
    return render(request, '19.File_Uploading.html')


def Display_Uploaded_File(request):
    dis = FileModel.objects.all()
    return render(request, '20.Display_Uploaded_File.html', {'dis': dis})


def Book_List(request):
    book = BookModel.objects.all()
    paginator = Paginator(book, 4)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, '21.Book_List.html', {'books': books})


def Add_Book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()
    return render(request, '22.Add_Book.html', {'form':form})


def Edit_Book(request, pk):
    book = BookModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(instance=book)
    return render(request, '22.Add_Book.html', {'form':form, 'book':book})


def Delete_Book(request, pk):
    book = BookModel.objects.get(pk=pk)
    book.delete()
    return redirect('/')


def Product_Search(request):
    query = request.GET.get('q')
    if query:
        result = BookModel.objects.all().filter(Q(Title__icontains=query)|Q(Author__Name__icontains=query)
                                                |Q(Genre__genre__icontains=query))
    else:
        result = []
    return render(request, '21.Book_List.html', {'books':result})


def Email_Send(request):
    if request.method == 'POST':
        to = request.POST.get('to')
        sub = request.POST.get('subject')
        msg = request.POST.get('msg')

        if to and sub and msg:
            r = send_mail(sub, msg, 'sreejith.techwingsys@gmail.com', [to])
            if r == 1:
                res = f'Email to {to}'
            else:
                res = 'Failed to send mail'
        else:
            res = 'Incomplete Form data'
        return render(request, '23.Email_Send.html', {'msg':res})
    elif request.method == 'GET':
        return render(request, '23.Email_Send.html', {'msg':''})

    else:
        return HttpResponse('Method not allowed', status=405)


def Email_Attach(request):
    if request.method == 'POST':
        form = MailForm(request.POST, request.FILES)
        if form.is_valid():
            email_to = form.cleaned_data['email_to']
            sub = form.cleaned_data['sub']
            msg = form.cleaned_data['msg']
            attach = request.FILES.get('attach')

            email = EmailMessage(sub, msg, 'sreejith.techwingsys@gmail.com', [email_to])
            if attach:
                email.attach(attach.name, attach.read(), attach.content_type)
            email.send()
            res = f'Emailed to {email_to}'
        else:
            res = 'Failed to send mail'
    else:
        form = MailForm()
        res = None
    return render(request, '24.Email_Attach.html', {'form':form, 'msg':res})


def Cookies(request):
    v = int(request.COOKIES.get('visit', 0))
    visit = v+1
    res = render(request, '25.Cookies.html', {'visit':visit})
    res.set_cookie('visit', visit)
    return res



# List all students
class StudentListView(ListView):
    model = Student
    template_name = "Students_Details/student_list.html"
    context_object_name = "students"


# Show Student details
class StudentDetailView(DetailView):
    model = Student
    template_name = "Students_Details/student_detail.html"
    context_object_name = "student"


# Create a new student
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "Students_Details/student_form.html"
    success_url = reverse_lazy('student_list')


# Update Student Details
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'Students_Details/student_form.html'
    success_url = reverse_lazy('student_list')


# Delete a student
class StudentDeleteView(DeleteView):
    model = Student
    template_name = "Students_Details/student_confirm_delete.html"
    success_url = reverse_lazy('student_list')

