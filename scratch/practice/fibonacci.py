def fib(n):
    if n < 0:
        return -1

    if n == 1 or n == 2:
        return n-1

    first = 0
    second = 1
    number = 0

    for i in range(3, n+1):
        number = first + second
        first = second
        second = number

    return number
