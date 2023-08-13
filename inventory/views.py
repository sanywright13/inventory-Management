from django.shortcuts import render ,redirect
from django.http import HttpRequest
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView , View
from .forms import UserRegisterForm , AddItemForm
from .models import InventoryItem,Category
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Index(TemplateView):
    template_name="inventory/index.html"

class DashboardView(LoginRequiredMixin,View):
    login_url = '/inventory/login/'
    def get(self,request):
        Useritmes=InventoryItem.objects.filter(user=self.request.user.id).order_by('id')
        return render(request,'inventory/dashboard.html',{'items':Useritmes})
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
        
class CreateItemView(LoginRequiredMixin,CreateView):
    template_name='inventory/AddItem_form.html'
    form_class=AddItemForm
    success_url='/inventory/dashboard/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context['name']='sanaa'
        return context
    
    def form_valid(self,form):
        print(form)
        form.instance.user=self.request.user
        return super().form_valid(form)
                