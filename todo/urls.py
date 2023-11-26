from django.urls import path

from .views import TodoListView, TodoCreateView, TodoDeleteView, TodoUpdateView

urlpatterns = [
    path("list/", TodoListView.as_view(), name='todo-list'),
    path("create/", TodoCreateView.as_view(), name='todo-create'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo-delete'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='todo-update'),

]