from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
	path('signup', views.SignupView.as_view(), name='signup_form'),
	path('registrated', views.RegistrationCompleted.as_view(), name='registration_completed'),
	path('login', views.LoginView.as_view(), name='login_form'),

]
