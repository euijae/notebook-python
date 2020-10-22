def function_bang():
    print('function_bang! before')
    raise ValueError('Bang!')
    print('function_bang! after')


try:
    function_bang()
except ValueError as ve:
    print(ve)
    # raise
