strings = ['do', 're', 'mi']

result = ','.join(strings)
print(result)

# joiner joins when the size(arr) > 1
result = 'b'.join(['a'])
print(result)  # result = 'a'

result = 'b'.join(['a', 'a'])
print(result)  # result = 'aba'
