from django import forms
from .models import MyEmail








class EmailForm(forms.ModelForm):
    class Meta:
        model = MyEmail
        fields = ['name', 'subject', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter the subject'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        }
