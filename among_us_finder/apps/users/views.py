from .forms import SignupForm
from django.views.generic.edit import FormView


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm

