from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from posts.models import Author

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'bio', 'profile_pic']
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['fullname'].required = True
        # self.fields['profile_pic'].required = True

