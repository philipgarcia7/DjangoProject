from tkinter import Widget
from django import forms

from .models import Pizza,Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['pizza_name']
        labels = {'pizza_name':''}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['topping_name']
        labels = {'topping_name':''}
        widgets = {'topping_name': forms.Textarea(attrs={'cols':80})}