from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .forms import UserForm


# Create your views here.



class HomeViews(TemplateView):
    template_name = "home/landing.html"

class LogInViews(View):
    template_name = "home/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home_app:home')
        context = {}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home_app:home')
        return self.get(request)


class SignUpViews(View):
    template_name = "home/signup.html"


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_app:home')
        context = {
            'errors': kwargs.get('errors'),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        form = UserForm(request.POST)
        
        if form.is_valid():
            
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']
        


            
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                #password=password,
            )

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home_app:home')
        return self.get(request, errors=form.errors)

class LogOutViews(View):

    def get(self, request):
        logout(request)
        return redirect('home_app:home')
