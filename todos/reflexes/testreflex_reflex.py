from sockpuppet.reflex import Reflex


class TestreflexReflex(Reflex):
    def increment(self, step=1):
        self.count = int(self.element.dataset['count']) + step
