from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import *

app_name = "main"
urlpatterns = [
    path('', homeView, name='quiz'),
    path('quiz/', QuizView.as_view(), name='quiz'),

    # accounts path
    path("login/", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path("register/", register, name='register'),
    
    path("profile/", profile, name='profile'),
    path("update/<pk>", UpdateProfileView.as_view(), name='update'),

    # check answer
    path("check/", check, name='check'),

    #congratulation
    path("congratulation/", congratulation.as_view(), name='priz')
]