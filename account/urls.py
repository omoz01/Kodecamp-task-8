from django.urls import path
from .views import signup, booking
from django.contrib.auth import views as new_views

app_name = "account"

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", new_views.LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout/", new_views.LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path("booking/", booking, name="booking"),
]