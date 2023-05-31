from django import forms
from django.forms import ModelForm
from .models import Book
from .models import Comment
from django.forms import ModelForm, TextInput, EmailInput, Textarea


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', ]
        widgets = {
            'body': Textarea(attrs={
                'style': 'max-width:600px; max-height:50px;'
                         'width:85%; margin: 0 auto; background-color:#C2C5AA;'
                         ,
                'class': "form-control mb-3",
            }),
        }
        labels = {
            'body': '',
        }




