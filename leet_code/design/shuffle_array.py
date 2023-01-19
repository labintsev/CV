import random
from typing import List


class Solution:
    def __init__(self, nums):
        self.nums = nums[:]
        self.copy = nums[:]

    def reset(self):
        self.nums = self.copy[:]
        return self.nums

    def shuffle(self):
        n = len(self.nums)
        for i in range(n):
            j = random.randint(i, n - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


def equal(a1: List[int], a2: List[int]) -> bool:
    for x1, x2 in zip(a1, a2):
        if x1 != x2:
            return False
    return True


if __name__ == '__main__':
    a = [1, 2, 3]
    print(a)
    solution = Solution(a)
    a1 = solution.shuffle()
    print('Shuffled: ', a1)
    a2 = solution.reset()
    print('Reset: ', a2)
    a3 = solution.shuffle()
    print('Shuffled: ', a3)
    assert equal(a, a2)
    assert not equal(a, a1)
    assert not equal(a1, a3)
