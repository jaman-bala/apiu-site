from .models import Create
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput



class CreateForm(ModelForm):
    class Meta:
        model = Create
        fields = ['first_name', 'last_name', 'email', 'city' ,'phone', 'title', 'text', 'file']

        widgets = {
            "first_name": TextInput(attrs={
              
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
    
                'placeholder': 'Фамилия'
            }),
            "phone": TextInput(attrs={

                'placeholder': '+996 '
            }),
            "email": TextInput(attrs={

                'placeholder': 'Адрес электронной почты'
            }),
            "city": TextInput(attrs={

                'placeholder': 'Адрес'
            }),
            "title": TextInput(attrs={

                'placeholder': 'Вопроса'
            }),
            "text": Textarea(attrs={

                'placeholder': 'Введите свой вопрос'
            }),
            "file": FileInput(attrs={

                'placeholder': 'Файл'
            }),


        }