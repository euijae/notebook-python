import Shape


class Circle(Shape):
    def __init__(self, id):
        super().__init__(id)

    def display(self):
        print('Circle:', self._id)

    @property
    def id(self):
        """ the id property """
        return self._id


c = Circle('circle1')
print(c.id)
c.display()
