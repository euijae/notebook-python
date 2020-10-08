'''
string[start:end:step]
'''
str = "0123456789"

print("str[0:4]", str[0:4])
print("str[1:7]", str[1:7])
print("str[8:len(str)]", str[100:len(str)] == '')

# forward step
print("str[0:7]", str[0:7])
print("str[0:7:2]", str[0:7:2])

# negative step
print("str[10:2:-1]", str[10:2:-1])  # 9876543
print("str[10:0:-2]", str[10:0:-2])  # 97531

# Partial slicing
print("str[:8]", str[:8])  # all the characters before 8th - 0...7
print("str[8:]", str[8:])  # all the characters starting from 8th - 89
print(str[::-1])  # The whole string in reverse
