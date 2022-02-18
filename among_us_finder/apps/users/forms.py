from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from among_us_finder.apps.users.models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'level_of_advancement')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username:'
        self.fields['username'].help_text = ''
        self.fields['email'].label = 'Email:'
        self.fields['password1'].label = 'Password:'
        self.fields['password1'].help_text = ''
        self.fields['password2'].label = 'Confirm the password:'
        self.fields['password2'].help_text = ''

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user


class LoginForm(AuthenticationForm):

    class Meta:
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username:'
        self.fields['password'].label = 'Password:'
