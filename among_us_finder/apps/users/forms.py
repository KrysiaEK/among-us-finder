from django.forms import ModelForm
from among_us_finder.apps.users.models import User


class SignupForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'level_of_advancement', 'password']
