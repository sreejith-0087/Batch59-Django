from django import forms
from .models import BookModel

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


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['Title', 'Author', 'Genre', 'Published_Date', 'Image']



class MailForm(forms.Form):
    email_to = forms.EmailField()
    sub = forms.CharField(max_length=200, label='Subject', min_length=10)
    msg = forms.CharField(widget=forms.Textarea, label='Message')
    attach = forms.FileField()