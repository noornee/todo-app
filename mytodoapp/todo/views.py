from django.shortcuts import render 
from django.urls import reverse_lazy
from .models import Todo
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm
from .custom_user_form import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.

class TodoRegisterForm(SuccessMessageMixin, FormView):
    template_name = 'todo/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo:todo_list')
    success_message = "your account was created successfully"

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(TodoRegisterForm, self).form_valid(form)    



class TodoLoginView(LoginView):
    template_name = 'todo/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo:todo_list')


class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todo_list'
    template_name = 'todo/index.html'
    ordering = ['-modified']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = context['todo_list'].filter(user=self.request.user)
        context['count'] = context['todo_list'].filter(complete=False).count()
        return context

class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo 
    template_name = 'todo/todo_detail.html'
    slug_field = 'slug'

class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = 'todo/todo_update.html'
    # fields = '__all__'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todo:todo_list')

class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo    
    template_name = 'todo/todo_delete.html'
    success_url = reverse_lazy('todo:todo_list')

class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = 'todo/todo_create.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todo:todo_list')  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)
