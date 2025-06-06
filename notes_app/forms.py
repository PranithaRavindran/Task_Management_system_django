from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Note

class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'bio', 'password1', 'password2')

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'priority', 'due_date', 'is_completed']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'content': forms.Textarea(attrs={'rows': 4}),
        }