import json
from datetime import datetime
from django.shortcuts import render ,redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import UpdateView
from django.core.paginator import Paginator
from .models import *
# Create your views here.
def homeView(request):
    return render(request, "index.html")



class QuizView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'quiz.html' 
    context_object_name = "Question"  

@login_required
def check(request):
    a = json.loads(request.GET['data'])
    true,false=0,0
    for i in a:
        if Answer.objects.get(id=i).is_right == True:
            true +=1
        else:
            false += 1
    b = Test(question=Quizzes.objects.get(id=i), true_answer=true, false_answer=false, all_answer=request.GET['length'])
    b.save()
    c = request.user.profile.rank.add(b)
    return JsonResponse({'success': 200}) 

login_required()
def congratulate(request):
    context = {
        'true' : request.user.profile.rank.last().true_answer,
        'false': request.user.profile.rank.last().false_answer,
        'all': request.user.profile.rank.last().all_answer,
    }
    print()
    return render(request, 'congratulation.html', context)