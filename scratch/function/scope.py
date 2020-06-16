'''
    When mutable data is passed to a function,
    the function can modify or alter it.
    These modifications will stay in effect
    outside the function scope as well.
    An example of mutable data is a list.

    In the case of immutable data,
    the function can modify it,
    but the data will remain unchanged outside
    the function’s scope.
    Examples of immutable data are numbers, strings, etc.
'''

num = 20


def multiply_by_10(n):
    n *= 10
    num = n
    print("Value of num inside:", num)
    return n


multiply_by_10(num)
print("Value of num outside:", num)
