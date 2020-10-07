def trace(method):
    def method_wrapper(self, x, y):
        print('Calling', method, 'with', x , y)
        method(self, x, y)
        print('Called', method, 'with', x, y)

    return method_wrapper

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @trace
    def move_to(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point - ' + str(self.x) + ', ' + str(self.y)


p = Point(1, 1)
print(p)
p.move_to(5, 5)
print(p)
