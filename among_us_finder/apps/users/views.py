from django.shortcuts import redirect
from django.urls import reverse

from .forms import SignupForm, LoginForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = 'registrated'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegistrationCompleted(TemplateView):
    template_name = 'users/registration_completed.html'


class MyLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)  # here method should be GET or POST.
        if next_url:
            return "%s" % (next_url)  # you can include some query strings as well
        return reverse('rooms:room_list')


class MyLogoutView(LogoutView):

    def logout_view(request):
        logout(request)

"""
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs['host'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""
