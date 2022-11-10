from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from .models import Profile
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save(force_insert=False)
            Profile.objects.create(user=user)
            auth.login(request,user)
            return redirect('/profile/')
    else:
        form = UserRegisterForm()
    return render(request, "account/register.html", {"form":form})

@login_required(login_url="/login/")
def profile(request):
    u = request.user
    user = Profile.objects.get(user=u)
    if user:
        return render(request, "account/detail.html", {"user": user})
    else:
        return render(request, "account/detail.html")



def edit(request,user_id):
    if request.method == "POST":
        profile_edit_form = ProfileEditForm(request.POST)
        if profile_edit_form.is_valid():
            profile_edit_form.save()
            return redirect("/profile/")
    else:

        profile_edit_form = ProfileEditForm()

    context = {
        "form":profile_edit_form
    }
    return render(request, "account/edit.html", context)


class UpdateProfileView(LoginRequiredMixin,UpdateView):
    model = Profile
    fields = ["date_of_birth","photo","short_info",]
    template_name = 'account/edit.html'
    success_url = "/profile"
    # slug_field = 'username'
    # slug_url_kwarg = 'slug'

    def get_object(self):
        user = Profile.objects.get(user=self.request.user)
        return user