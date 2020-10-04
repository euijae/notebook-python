def kids_with_candies(candies, extra_candies):
    max_candy = 0

    for candy in candies:
        if candy > max_candy:
            max_candy = candy

    results = []

    for candy in candies:
        results.append(candy + extra_candies >= max_candy)

    return results


def kids_with_candies2(candies, extra_candies):
    max_candy = max(candies)

    return [extra_candies + candy >= max_candy for candy in candies]


print(kids_with_candies([2, 3, 5, 1, 3], 3))
print(kids_with_candies2([2, 3, 5, 1, 3], 3))
