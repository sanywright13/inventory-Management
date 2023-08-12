from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=80)
    age=models.IntegerField()
class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(slf):
        return self.name
class InventoryItem(models.Model):
    name=models.CharField(max_length=200)
    quantity=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    

        