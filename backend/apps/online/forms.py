from .models import Create
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NumberInput, FileInput



class CreateForm(ModelForm):
    class Meta:
        model = Create
        fields = ['first_name', 'last_name', 'email', 'phone', 'title', 'text', 'file', 'date']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'input-group-text',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'input-group-text',
                'placeholder': 'Фамилия'
            }),
            "phone": NumberInput(attrs={
                'class': 'input-group-text',
                'placeholder': 'Номер телефона'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес электронной почты'
            }),
            "title": TextInput(attrs={
                'class': 'input-group-text',
                'placeholder': 'Название вопроса'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            "file": FileInput(attrs={
                'class': 'input-group-text',
                'placeholder': 'Текст'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'type': "date",
                'placeholder': 'Дата'
            }),

        }