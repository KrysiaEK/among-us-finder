from .forms import SignupForm, LoginForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = 'registrated'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegistrationCompleted(TemplateView):
    template_name = 'users/registration_completed.html'


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
