from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from among_us_finder.apps.users.models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'level_of_advancement']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username:'
        self.fields['username'].help_text = ''
        self.fields['email'].label = 'Email:'
        self.fields['password1'].label = 'Password:'
        self.fields['password1'].help_text = ''
        self.fields['password2'].label = 'Confirm the password:'
        self.fields['password2'].help_text = ''

    def save(self, *args, **kwargs):
        print('sfsdfdasdfd')
        return super(SignupForm, self).save(*args, **kwargs)


class LoginForm(AuthenticationForm):

    class Meta:
        fields = ['username', 'password']
