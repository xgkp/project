from django import forms
from django.core.validators import RegexValidator

from newbook.models import Author

class MessageForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=20, required=True,error_messages={
        'required': 'Title is required.',
        'min_length': 'Title must be at least 3 characters long.',
        'max_length': 'Title cannot exceed 20 characters.'
    })
    content = forms.CharField(min_length=10, max_length=30, required=True, error_messages={
        'required': 'Content is required.',
        'min_length': 'Content must be at least 10 characters long.',
        'max_length': 'Content cannot exceed 200 characters.'
    }, widget=forms.Textarea)

class RegisterForm(forms.Form):
    telphone = forms.RegexField(
        regex=r'^1[3-9]\d{9}$',
        error_messages={
            'invalid': 'Enter a valid phone number.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )
    pwd1 = forms.CharField(
        min_length=6,
        max_length=20,
        error_messages={
            'required': 'Password is required.',
            'min_length': 'Password must be at least 6 characters long.',
            'max_length': 'Password cannot exceed 20 characters.'
        },
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

    pwd2 = forms.CharField(
        min_length=6,
        max_length=20,
        error_messages={
            'required': 'Please confirm your password.',
            'min_length': 'Password must be at least 6 characters long.',
            'max_length': 'Password cannot exceed 20 characters.'
        },
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
    )

    def clean_telphone(self):
        telphone = self.cleaned_data['telphone']
        # Additional custom validation logic can be added here if needed
        exists = Author.objects.filter(telphone=telphone).exists()
        if exists:
            raise forms.ValidationError("This phone number is already registered.")
        return telphone
    
    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')

        if pwd1 and pwd2 and pwd1 != pwd2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data