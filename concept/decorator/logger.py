def logger1(func):
    def inner():
        print('calling', func.__name__)
        func()
        print('returned from', func.__name__)

    return inner

def logger2(func):
    def inner(x, y):
        print('calling', func.__name__, 'with', x, 'and', y)
        func(x,y)
        print('returned from', func.__name__)

    return inner

@logger1
def target():
    print('in target function')

@logger2
def my_func(x, y):
    print(x, y)

my_func(4,5)
