class Quantity:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        new_value = self.value + other.value
        return Quantity(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Quantity(new_value)

    def __str__(self):
        return 'Quantity[' + str(self.value) + ']'

    """
    eq, lt, le, gt, ge,
    add, sub, truediv,
    floordiv, mod, rshift,
    lshift, pow, mult
    """


q1 = Quantity(10)
q2 = Quantity(2)
q3 = q1 - q2
print(q3)
