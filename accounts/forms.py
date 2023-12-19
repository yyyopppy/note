# class UserCreationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ("username",)

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.hashers import make_password



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


