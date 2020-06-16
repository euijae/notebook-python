def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1*n2


def div(n1, n2):
    return n1/n2


def calculator(ops, n1, n2):
    return ops(n1, n2)


print("calculator(mult, 10, 20):", calculator(mult, 10, 20))
print("calculator(add, 10, 20):", calculator(add, 10, 20))


result = calculator(lambda n1, n2: n1 * n2, 10, 20)
print(result)
print(calculator(lambda n1, n2: n1 + n2, 10, 20))

# This creates a new list. The original list remains unchanged.
num_list = [0, 1, 2, 3, 4, 5]
double_list = map(lambda n: n * 2, num_list)
print(list(double_list))

greater_than_2 = list(filter(lambda n: n > 2, num_list))
print(greater_than_2)
print(num_list)
