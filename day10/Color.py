from enum import Enum, unique
from random import randint


@unique
class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    Blue = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)
