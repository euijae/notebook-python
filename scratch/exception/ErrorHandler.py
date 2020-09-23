def runcalc(value):
    value / 0


try:
    runcalc(6)
except IndexError:
    print('index')
except ZeroDivisionError as exp:
    print(exp)
    print('oops')
