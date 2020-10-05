from typing import List


def num_identical_pairs(nums: List[int]) -> int:
    counter = 0
    num_pairs = {}

    for num in nums:
        num_pairs[num] = (num_pairs[num] + 1 if num in num_pairs else 1)

    for k, v in num_pairs.items():
        counter += (v-1)*v / 2

    return int(counter)


print(num_identical_pairs([1, 2, 3, 1, 1, 3]))
