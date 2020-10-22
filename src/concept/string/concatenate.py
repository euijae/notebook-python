result = 'a' + 'b' + 'c'
print(result)

result = 'do' * 2
print(result)

result = 'Hello'
result += ', world'

print(result)

# Compile error! Python doesn't allow this
try:
    result = 'Hello' + 2
except TypeError as te:
    print(te)
