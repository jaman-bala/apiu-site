from .models import Create
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NumberInput, FileInput



class CreateForm(ModelForm):
    class Meta:
        model = Create
        fields = ['first_name', 'last_name', 'email', 'phone', 'title', 'text', 'file', 'date']

        widgets = {
            "first_name": TextInput(attrs={
              
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
    
                'placeholder': 'Фамилия'
            }),
            "phone": NumberInput(attrs={

                'placeholder': '+996 '
            }),
            "email": TextInput(attrs={

                'placeholder': 'Адрес электронной почты'
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
            "date": DateTimeInput(attrs={

                'type': "date",
                'placeholder': 'Дата'
            }),

        }