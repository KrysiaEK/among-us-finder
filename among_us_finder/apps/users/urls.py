from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
	path('signup', views.SignupView.as_view(), name='signup_form'),
	path('registrated', views.RegistrationCompleted.as_view(), name='registration_completed'),
	path('login', views.MyLoginView.as_view(), name='login_form'),
	path('logout', views.MyLogoutView.as_view(), name='logout_form'),
]
