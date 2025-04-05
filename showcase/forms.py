from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Your name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input',
            'placeholder': 'your@email.com'
        })
    )
    subject = forms.CharField(
        max_length=35,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Subject'
        })
    )
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'textarea',
            'placeholder': 'Say something...',
            'rows': 4
        })
    )
