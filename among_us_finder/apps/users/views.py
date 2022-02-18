from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout

from among_us_finder.apps.users.forms import SignupForm, LoginForm


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = 'registered'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class RegistrationCompleted(TemplateView):
    template_name = 'users/registration_completed.html'


class MyLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return "%s" % (next_url)
        return reverse('rooms:room_list')


class MyLogoutView(LogoutView):

    def logout_view(request):
        logout(request)
