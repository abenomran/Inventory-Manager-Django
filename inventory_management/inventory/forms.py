from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import InventoryItem, Category

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InventoryItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
        # this is called a form field, check django documentation for best one to use in given scenario
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'category', ]
        # fields = '__all__' would get all fields of the model. we don't want our user field so we don't do that here
        # and date created is automatically set, so we don't need it either. 
