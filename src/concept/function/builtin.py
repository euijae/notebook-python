'''
    Search.
    An alternative for finding a substring using the in keyword
    is the find() method. It returns the first index at which
    a substring occurs in a string. If no instance of
    the substring is found, the method returns -1.

    find(substring, start, end)
    - start, end = optional
'''
str1 = "0123456789"
print('Given string:', str1)
print("str1.find('23'):", str1.find('23'))
print("str1.find('23', 0, 4):", str1.find('23', 2, 4))


'''
    Replace
    The original string is not altered.
    Instead, a new string with the replaced
    substring is returned. Case sensitive.
    Replace all strings if they are matched.
'''
str1 = "Welcome to Hello World! Welcome to Bye World!"
new_str = str1.replace("Welcome to", "Greetings from")
print("str:", str1)
print("new_str:", new_str)

''' upper and lower '''

''' int() '''
print("int('12')*10:", int("12")*10)
print("int(20.5):", int(20.5))
print("int(False):", int(False))

'''
    ord(): Convert a character to its Unicode value
    Return the Unicode code point for a one-character string.
'''
print("ord('a'):", ord('a'))  # 97
print("ord('0'):", ord('0'))  # 48


''' float() '''
print("float(24):", float(24))
print("float('24.5'):", float('24.5'))
print("float(True):", float(True))

''' str() '''
print("str(12) + '.345':", str(12) + '.345')
print("str(False)", str(False))
print("str(12.345) + ' is a string':", str(12.345) + ' is a string')

'''
    bool()
    Strings are always converted to True.
    Floats and integers with a value of zero
    are considered to be False in Boolean terms
'''
print("bool(10):", bool(10))
print("bool(0.0):", bool(0.0))
print("bool('Hello'):", bool("Hello"))
