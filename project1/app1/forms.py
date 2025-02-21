from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    subject = forms.CharField(max_length=50)
    email = forms.CharField(max_length=30)


class InfoForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    addr = forms.CharField(max_length=40)
    phone = forms.IntegerField()


class RegisterForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Phone = forms.IntegerField()
    Email = forms.EmailField()
    Password = forms.CharField(max_length=25)

class LoginForm(forms.Form):
    Email = forms.EmailField()
    Password = forms.CharField(max_length=25)

class FileForm(forms.Form):
    File_Name = forms.CharField(max_length=50)
    File = forms.ImageField()
