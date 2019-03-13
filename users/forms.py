from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from django.db import transaction
#from django.forms.utils import ValidationError
#from .models import User




# Form for consultant with additional email field

class ConsultantSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_consultant = True
        if commit:
            user.save()
        return user




# Form for learner with additional email field

class LearnerSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_learner = True
        if commit:
            user.save()
        return user

#    class Meta(UserCreationForm.Meta):
#        model = User
