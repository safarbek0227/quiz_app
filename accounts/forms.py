from timeit import repeat
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'input', 'placeholder':'password'}))
    repeat_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class':'input', 'placeholder':'Repeat password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')
        widgets = {
            "username":forms.widgets.TextInput(attrs={'class':'input', 'placeholder':'username'}),
            "first_name":forms.widgets.TextInput(attrs={'class':'input', 'placeholder':'First name'}),
            "last_name":forms.widgets.TextInput(attrs={'class':'input', 'placeholder':'last name'}),
            'email':forms.EmailInput(attrs={'class':'input', 'placeholder':'email'}),

        }



    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['repeat_password']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo', "short_info",)
        widgets = {
            "short_info":forms.Textarea(attrs={"cols": 3,"rows":3}),
            "date_of_birth":forms.DateInput(format='%d/%m/%Y', attrs={"type": "date",})
        }