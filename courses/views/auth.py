from django.shortcuts import render , redirect
from courses.models import Course ,Video
from django.shortcuts import HttpResponse
#create ur views here 
from django.contrib.auth import logout ,login
from django.views import View
from courses.forms import RegistrationForm , Loginform
from django.views.generic.edit import FormView

class SignupView(FormView):
    template_name="courses/signup.html"
    form_class = RegistrationForm
    success_url = '/login'
    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
     
class LoginView(FormView):
    template_name="courses/login.html" 
    form_class = Loginform
#    success_url  = '/'
    success_url  = '/index'

    def form_valid(self, form):
        login(self.request , form.cleaned_data)
        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect(next_page)
        return super().form_valid(form)
    
def signout(request):
    logout(request)
#    return redirect("home")
    return redirect("index")