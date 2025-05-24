# forum/forms.py
from django import forms
from .models import ForumPost

class ForumPostForm(forms.ModelForm):
    class Meta:
        model  = ForumPost
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Napisz coś…'
            }),
        }
