n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]
result = ()
found = False

for n1 in num_list:
    for n2 in num_list:
        if(n1 + n2 == n):
            result = (n1, n2)
            found = True
            break
    if found:
        break

print(result)


num_list = list(range(0, 10))

for num in num_list:
    if num == 3 or num == 6 or num == 8:
        continue
    print(num)


class Test:
    pass
