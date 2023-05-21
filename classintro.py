class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(1, 2)
print(point1.draw())


point2 = Point(10, 20)
point2.x = 22090
print(point2.x)
