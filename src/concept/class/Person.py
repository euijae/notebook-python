
class Person:
    """An example class to hold a
        persons name and age"""

    instance_count = 0

    def __init__(self, name, age):
        Person.increment_instance_count()
        self._name = name
        self._age = age

    @property
    def age(self):
        print('In age method')
        return self._age

    @age.setter
    def age(self, value):
        print('In set_age method')
        if isinstance(value, int) & value > 0 & value < 120:
            self._age = value

    @property
    def name(self):
        print('In name')
        return self._name

    @name.deleter
    def name(self):
        del self._name

    def __str__(self):
        return 'Person[' + self._name + '] is ' + str(self._age)

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1

    @staticmethod
    def static_function():
        print('static function')


p1 = Person('Euijae', 34)
print(p1)
