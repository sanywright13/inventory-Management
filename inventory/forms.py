from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import InventoryItem , Category
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
        
class AddItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = InventoryItem
        fields=['name','quantity','category']
        #we need the category form to add it
        '''
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["categories"].queryset = Catgory.objectcis.all() 
        '''     