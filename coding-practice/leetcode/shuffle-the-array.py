from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:

    result_arr = list()

    for index in range(n):
        result_arr.append(nums[index])
        result_arr.append(nums[index+n])

    return result_arr


print(shuffle([2, 5, 1, 3, 4, 7], 3))
