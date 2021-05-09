from sockpuppet import reflex
from sockpuppet.channel import Channel

from todos.models import Todo


class TodoReflex(reflex.Reflex):
    def add_todo(self, step=1):
        Todo.objects.create(description='NewReflexTest')
        channel_id = self.get_channel_id()

        channel = Channel(name=channel_id, identifier='{"channel":"StimulusReflex::Channel"}')
        channel.morph({
            'selector': '#todo-counter',
            'html': 'hello',
            'children_only': True,
        })
        channel.broadcast()

    def reload(self):
        pass
