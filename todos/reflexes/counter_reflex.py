from sockpuppet import reflex

from todos.models import Todo


class CounterReflex(reflex.Reflex):
    def increment(self, step=1):
        Todo.objects.create(description='ReflexTest')
