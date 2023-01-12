from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        p = 0
        nums = sorted(nums)
        while p < len(nums) // 2:
            if nums[2*p] != nums[2*p+1]:
                return nums[2*p]
            p += 1
        return nums[-1]


if __name__ == '__main__':
    s = Solution()
    assert s.singleNumber([2, 2, 1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
    assert s.singleNumber([1]) == 1
