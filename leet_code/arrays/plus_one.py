from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = len(digits) - 1
        r = 1
        while r == 1 and p >= 0:
            digits[p] += r
            if digits[p] == 10:
                digits[p] = 0
                r = 1
            else:
                r = 0
            p -= 1
        if r == 1:
            digits = [1] + digits
        return digits


if __name__ == '__main__':
    s = Solution()
    ans = s.plusOne([2, 2, 1])
    assert ans == [2, 2, 2], ans
    ans = s.plusOne([4, 9])
    assert ans == [5, 0], ans
    ans = s.plusOne([9, 9])
    assert ans == [1, 0, 0], ans
    ans = s.plusOne([9])
    assert ans == [1, 0], ans
    ans = s.plusOne([0])
    assert ans == [1], ans
