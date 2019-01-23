from django import forms
from home.models import MyUser


class SignupForm(forms.ModelForm):
    class Meta:
        model = MyUser

        fields = [
            'first_name',
            'last_name',
            'username',
            'gender',
            'email',
            'phone_number',
            'password',
        ]