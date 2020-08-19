from django.shortcuts import render
from django.views.generic import FormView,TemplateView
from two_factor.views import ProfileView
from two_factor.views.utils import class_view_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .form import SignUp


@class_view_decorator(never_cache)
@class_view_decorator(login_required)
class Profile(ProfileView):
    template_name = 'home.html'

def my_view(request):
    return render(request,'secret.html')

def logout_(request):
    logout(request)
    return HttpResponseRedirect('/2f/account/login')

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('emails')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return HttpResponseRedirect('/2f/account/login')
    else:
        form = SignUp()
    return render(request, 'signup.html', {'form': form})
