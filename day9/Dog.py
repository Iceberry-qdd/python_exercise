from Pet import Pet


class Dog(Pet):
    def make_voice(self):
        print('%s:汪汪汪...' % self._nickname)
