def number_of_steps(num: int) -> int:
    count = 0

    while num != 0:
        num = int(num / 2) if (num % 2 == 0) else num - 1
        count = count + 1

    return count


print(number_of_steps(14))
