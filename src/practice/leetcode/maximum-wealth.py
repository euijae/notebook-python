from typing import List


def maximum_wealth(self, accounts: List[List[int]]) -> int:
    result = 0
    for account in accounts:
        inner_sum = 0
        for element in account:
            inner_sum = inner_sum + element

        result = max(inner_sum, result)

    return result

