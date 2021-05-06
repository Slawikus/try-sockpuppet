from django.views.generic.base import TemplateView


class TestreflexView(TemplateView):
    template_name = 'testreflex.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = 0
        return context
