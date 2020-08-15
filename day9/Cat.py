from Pet import Pet


class Cat(Pet):
    def make_voice(self):
        print('%s:喵喵喵...' % self._nickname)
