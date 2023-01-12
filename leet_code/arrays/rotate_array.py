from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0 or len(nums) == 1:
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        # print(nums)


nums = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    s = Solution()
    s.rotate(nums, 10)

    assert nums == [3, 4, 5, 1, 2]
