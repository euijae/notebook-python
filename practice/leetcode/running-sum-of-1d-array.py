from typing import List


def running_sum(nums: List[int]):
    acc = 0
    for index, num in enumerate(nums, start=0):
        nums[index] += acc
        acc += num

    return nums


def running_sum2(nums: List[int]) -> List[int]:
    for index in range(1, len(nums)):
        nums[index] += nums[index - 1]

    return nums

