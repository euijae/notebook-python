'''
    Variables are mutable
    first, is assigned to another variable,
    second, its value is copied into second.
    Hence, if we later change the value of first,
    second will remain unaffected
'''
first = 20
second = first
first = 35

print(first, second)
