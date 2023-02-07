from django import forms
from . models import Contact
from . models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 25})
        }

class MessageForm(forms.ModelForm):
    class Meta: 
        model = Message
        fields = ['name', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'cols': 25})
        }