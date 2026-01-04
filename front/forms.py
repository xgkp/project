from django import forms

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