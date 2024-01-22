from django import forms
from django.core.exceptions import ValidationError
import re

def validate_custom_email(value):
    # Define your custom regex pattern
    pattern = re.compile(r'^(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{6,}$')
    
    # Use the regex pattern to match the email
    if not pattern.match(value):
        raise ValidationError('Enter a valid email address with at least 1 special character and a minimum length of 6 characters.')

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),validators=[validate_custom_email],error_messages={'invalid': 'Custom error message for invalid email.'})
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cnic = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your CNIC'}))
    mobile_no = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Mobile No.'}))
    nationality = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Nationality','value':'Pakistan'}))
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
        
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}),
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18 or age > 120:
            raise ValidationError("Age must be between 18 and 120.")
        return age

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
