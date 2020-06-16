'''
    lambda is an anonymous function that returns something
'''
triple = lambda num : num * 3
print(triple(10))

concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
print(concat_strings("World", "Wide", "Web"))

my_func = lambda num: "High" if num > 50 else "Low"
print(my_func(30))
