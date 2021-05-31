from django.urls import path
from django.contrib.auth.views import LogoutView 
from .views import TodoList, TodoDetail, TodoUpdate, TodoDelete, TodoCreate, TodoLoginView, TodoRegisterForm

app_name = 'todo'

urlpatterns = [
    path('register',TodoRegisterForm.as_view(),name='register'),
    path('login/',TodoLoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(next_page='todo:login'),name='logout'),
    path('',TodoList.as_view(),name='todo_list'),
    path('create/',TodoCreate.as_view(),name='todo_create'),
    path('todo/<int:pk>/',TodoDetail.as_view(),name='todo_detail'),
    path('edit/<int:pk>/',TodoUpdate.as_view(),name='todo_edit'),
    path('delete/<int:pk>/',TodoDelete.as_view(),name='todo_delete')
]