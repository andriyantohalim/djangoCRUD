from django import forms
from .models import Book


class GeeksForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = [
            "title",
            "author",
            "abstract",
            "price"
        ]
