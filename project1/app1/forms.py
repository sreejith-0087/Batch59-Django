from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    subject = forms.CharField(max_length=50)
    email = forms.CharField(max_length=30)
