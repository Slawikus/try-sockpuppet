from sockpuppet import reflex


class CounterReflex(reflex.Reflex):
    def increment(self, step=1):
        self.session['count'] = int(self.session['count']) + step
