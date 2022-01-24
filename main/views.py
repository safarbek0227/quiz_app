import json
from datetime import datetime
from django.shortcuts import render ,redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import UpdateView
from django.core.paginator import Paginator

from .models import *


# Create your views here.
@login_required(login_url="/login/")
def homeView(request):
    return render(request, "index.html")

class QuizView(ListView):
    model = Question
    template_name = 'quiz.html' 
    context_object_name = "Question"  
    paginate_by = 1  



# accoun views 
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)

            return redirect("/profile")
    else:
        form = UserRegisterForm()
        form.add_placeholder()
    return render(request, "account/register.html", {"form":form})

@login_required(login_url="/login/")
def profile(request):
    u = request.user
    user = Profile.objects.get(user=u)
    if user:
        return render(request, "account/detail.html", {"user": user})
    else:
        return render(request, "account/detail.html")


class UpdateProfileView(UpdateView):
    model = Profile
    fields = ["date_of_birth", "short_info"]
    template_name = 'account/edit.html'
    success_url = "/profile"
def check(request):
    d = request.GET.get('data')
    data = json.loads(d)
    answer = Answer.objects.get(id=int(data))
    profile = request.user.profile
    if answer.is_right == True:
        profile.rank += 1
        profile.save()
    return JsonResponse({'success': 200})


class congratulation(TemplateView):
    template_name = "congratulation.html"