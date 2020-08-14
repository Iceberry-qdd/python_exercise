from math import sqrt


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other_point):
        dx = self.x-other_point.x
        dy = self.y-other_point.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3.5)
    p2 = Point()
    print(f'p1={p1}')
    print(f'p1={p2}')
    p2.move_by(-1, 2)
    print(f'After moved p1={p2}')
    print(f'distance from p1 to p2:{p1.distance_to(p2)}')


if __name__ == "__main__":
    main()
