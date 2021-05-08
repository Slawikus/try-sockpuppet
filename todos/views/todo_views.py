from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todos.forms import TodoCreateForm
from todos.models import Todo


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['todo_form'] = TodoCreateForm
        context['count'] = Todo.objects.count()

        return context


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoCreateForm
    template_name = 'todos/todo_create.html'
    success_url = reverse_lazy('todo_list')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ('description', 'due_date', 'is_completed')
    template_name = 'todos/todo_update.html'
    success_url = reverse_lazy('todo_list')
    context_object_name = 'todos'


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')
