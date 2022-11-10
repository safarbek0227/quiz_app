from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import *

app_name = "main"
urlpatterns = [
    path('', homeView, name='home'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('check/', check, name='check'),
    path('congratulate/', congratulate, name='congratulate')
]