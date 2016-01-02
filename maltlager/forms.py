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
