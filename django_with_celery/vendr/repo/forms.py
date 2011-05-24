from django import forms
import uuid

class UploadFileForm(forms.Form):
    uuid = forms.CharField(widget=forms.HiddenInput())
    filename = forms.FileField()

