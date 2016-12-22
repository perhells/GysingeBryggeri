from django import forms

class MaltForm(forms.Form):
    name = forms.CharField(max_length=20)
    amount = forms.FloatField()

class HopsForm(forms.Form):
    name = forms.CharField(max_length=20)
    amount = forms.FloatField()

class UpdateMaltForm(forms.Form):
    amount = forms.FloatField()

class UpdateHopsForm(forms.Form):
    amount = forms.FloatField()

class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

class BoardMemberForm(forms.Form):
    name = forms.CharField(max_length=200)
    role = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    image = forms.ImageField()

class ActivityForm(forms.Form):
    title = forms.CharField(max_length=200)
    date = forms.DateTimeField()
    content = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    mail = forms.CharField(max_length=200)
    content = forms.CharField(max_length=10000)
