class InvalidAgeException(Exception):
    """ valid ages between 0 and 120 """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'value: ' + self.value


class Person:
    def __init__(self, age):
        print('constructor')
        self._age = age

    @property
    def age(self):
        print('In age method')
        return self._age

    @age.setter
    def age(self, value):
        print('In setter')
        if isinstance(value, int) & value > 0 & value < 120:
            self._age = value
        else:
            raise InvalidAgeException(value)

    @age.deleter
    def age(self):
        del self._age

    def __str__(self):
        return 'age of ' + self._age


try:
    pe = Person(12)
    pe.age = -1
except InvalidAgeException as iae:
    print(iae)
