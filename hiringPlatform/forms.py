from .models import User, JobRole, UserRole
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# User to be filled form ->

class UserInterestedRolesForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = ['interested_roles', 'location_pref',
                  'current_CTC', 'expected_CTC']
        widgets = {
            'interested_roles': forms.CheckboxSelectMultiple,
        }
