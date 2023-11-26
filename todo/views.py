from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy, reverse


from .models import TodoModel
from .forms import TodoForm


class TodoListView(generic.ListView):
    model = TodoModel
    queryset = TodoModel.objects.all()
    template_name = 'todo/todo.html'
    context_object_name = 'todo'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["form"] = TodoForm()
        return context
    


class TodoCreateView(generic.CreateView):
    model = TodoModel
    from_class = TodoForm
    fields = ['title', 'text', 'time']
    success_url = reverse_lazy('todo-list')


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user


        return super().form_valid(form)



class TodoDeleteView(generic.DeleteView):
    model = TodoModel
    success_url = reverse_lazy('todo-list')


class TodoUpdateView(generic.UpdateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todo/todo.html'# از تمپلیت موجود استفاده شود
    success_url = reverse_lazy('task-list')
    queryset = TodoModel.objects.all()


    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        # obj = TodoModel.objects.filter(pk=context['pk'])

        print(context)
        context["form"] = TodoForm(
            # title=obj.title
        )
        return context
    


    