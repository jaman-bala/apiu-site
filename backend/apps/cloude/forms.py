from django import forms
from .models import Folder

from django import forms

class CreateFolderForm(forms.Form):
    name = forms.CharField(max_length=255)

class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    folder = forms.ModelChoiceField(queryset=Folder.objects.all())

