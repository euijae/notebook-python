def register(active = True):
    def wrap(func):
        def wrapper():
            print('Calling ', func.__name__, ' decorator param', active)

            if active:
                func()
                print('Called ', func.__name__)
            else:
                print('Skipped ', func.__name__)

        return wrapper
    return wrap

@register()
def func1():
    print('func1')

@register(active=False)
def func2():
    print('func2')

func1()
print('-' * 10)
func2()
