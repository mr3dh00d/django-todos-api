from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.getTodos, name='getTodos'),
    path('todos/<int:id>', views.getTodos, name='getTodos'),
    path('todos/create', views.createTodos, name='createTodos'),
    path('todos/update/<int:id>', views.updateTodos, name='updateTodos'),
    path('todos/delete/<int:id>', views.deleteTodos, name='deleteTodos')
]