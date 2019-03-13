
from django.shortcuts import render, redirect, reverse

from .forms import ConsultantSignUpForm, LearnerSignUpForm
from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView
from .models import User
from django.contrib.auth import login
#from django.db import transaction
#from django.db.models import Count
#from django.urls import reverse_lazy
#from blog import views as post_list
from django.contrib.auth.decorators import login_required
#from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
#View class for registration
class RegisterView(TemplateView):
    template_name = 'users/register.html'

#View for login
def home(request):
    if request.user.is_authenticated:
        if request.user.is_consultant:
            return redirect('post_list')
        else:
            return redirect('learn_post_list')
    return render(request, 'Login')

#View for Learner
class LearnerSignUpView(CreateView):
    model = User
    form_class = LearnerSignUpForm
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'learner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('firsthome')

#View for Consultant
class ConsultantSignUpView(CreateView):
    model = User
    form_class = ConsultantSignUpForm
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Consultant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('firsthome')

#View for Forget password
class Forgot(TemplateView):
    template_name = 'users/Forgot.html'

@login_required
def view_profile(request, pk=None):
    if pk:
        user = get_user_model(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'users/profile.html', args)

@login_required
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('view_profile')
            else:
                return redirect('change_password')
        else:
            form = PasswordChangeForm(user=request.user)

            args = {'form': form}
            return render(request, 'users/change_password.html', args)
