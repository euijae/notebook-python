"""
    Example of String split
    1. String is an immutable
    2. Can not be directly altered
"""

this_is_my_string = 'this is my string'
this_is_my_string_gaps = ' this   is  my string '

result = 'a,b,c'.split(',')
print(result)

result = this_is_my_string.split()
print(result)

# it cuts out leading and trailing whitespace
result = this_is_my_string_gaps.split()
print(result)

result = this_is_my_string_gaps.split('  ')
print(result)

print('  '.split(' '))  # result = ['', '']
print(' a'.split(' '))  # result = ['', 'a']

# @TODO compile error! why?
print(this_is_my_string.split(maxsplit=-1))
