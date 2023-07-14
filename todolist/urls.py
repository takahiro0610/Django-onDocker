from django.urls import path
from .views import TodoListView, TodoDetail

urlpatterns = [
    path('', TodoListView.as_view()),
    path('detail/<int:pk>', TodoDetail.as_view()),
]