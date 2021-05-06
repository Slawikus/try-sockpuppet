from django.views.generic.base import TemplateView

from todos.models import Todo


class CountView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = Todo.objects.count()

        return context
