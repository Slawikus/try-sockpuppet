from sockpuppet import reflex

from todos.models import Todo


class TodoReflex(reflex.Reflex):
    def add_todo(self, step=1):
        Todo.objects.create(description='NewReflexTest')

    def reload(self):
        pass
