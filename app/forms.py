from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Comment



class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    middle_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'middle_name', 'last_name', 'email', 'age', 'gender', 'phone_number', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove default help texts for specific fields
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class ProfileUpdateForm(forms.ModelForm):

    username = forms.CharField(max_length=150, required=True, label="Username")
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    middle_name = forms.CharField(max_length=30, required=False, label="Middle Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")
    email = forms.EmailField(label="Email Address")

    age = forms.IntegerField(min_value=18, required=True, label="Age")
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], required=True, label="Gender")
    phone_number = forms.CharField(max_length=15, required=True, label="Phone Number")

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'middle_name', 'last_name', 'email', 'age', 'gender', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.middle_name = self.cleaned_data['middle_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment here...'}),
        }



