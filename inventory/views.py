from django.shortcuts import render ,redirect
from django.http import HttpRequest
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView , View
from .forms import UserRegisterForm
# Create your views here.
class Index(TemplateView):
    template_name="inventory/index.html"
class DashboardView(View):
    def get(self,request):
        
        return render(request,'inventory/dashboard.html')
    def post(self,request):
        pass
        
class SignUpView(View):
    def get(self,request):
         form=UserRegisterForm()
         return render(request,'inventory/signup.html',{
             'form' :form
         })
    def post(self,request):
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('inventory:index')
        return render(request,'inventory/signup.html',{'form':form})
        
            