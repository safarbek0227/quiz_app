from django.contrib.auth.models import User
from .models import Profile
from django import forms

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')

    def add_placeholder(self):
        for field in self.fields:
            field = self.fields.get(field)
            field.widget.attrs.update({'placeholder': field.label})


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', )
        widgets = {
            "short_info":forms.Textarea(attrs={"cols": 3,"rows":3}),
            "date_of_birth":forms.DateInput(format='%d/%m/%Y', attrs={"type": "date"})
        }