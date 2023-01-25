"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""
import itertools
import time
from typing import List


def missing_numbers(nums: List[int]) -> int:
    for x, y in itertools.zip_longest(range(len(nums) + 1), sorted(nums)):
        if x != y:
            return x


def missing_numbers_2(nums: List[int]) -> int:
    n = len(nums)
    s = n * (n + 1) / 2
    s -= sum(nums)
    return int(s)


def test_case_1(f):
    assert missing_numbers([0, 1]) == 2
    assert missing_numbers([3, 0, 1]) == 2
    assert missing_numbers([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_case_2(f):
    t0 = time.time()
    f(list(range(10**7)))
    print('Test case take: ', time.time() - t0, ' s')


if __name__ == '__main__':
    test_case_1(missing_numbers_2)
    test_case_2(missing_numbers_2)
