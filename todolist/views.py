from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class TodoListView(TemplateView):
    template_name = "todolist.html"
    
