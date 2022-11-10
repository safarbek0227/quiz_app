from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .import views

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path("register/", views.register, name='register'),
    path("profile/", views.profile, name='profile'),
    path("edit/<int:user_id>", views.edit, name='edit'),
    path("update/", views.UpdateProfileView.as_view(), name='update')
]