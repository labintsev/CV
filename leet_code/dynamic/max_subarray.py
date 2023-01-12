from typing import List


def max_subarray(nums: List[int]) -> int:
    l = 0
    best_sum = nums[0]
    while l < len(nums) - 1:
        cur_sum = nums[l]
        for r in range(l+1, len(nums)):
            next_sum = cur_sum + nums[r]
            if next_sum >= cur_sum:
                cur_sum = next_sum
            else:
                l = r
                break
        best_sum = max(best_sum, cur_sum)
        l += 1
    return best_sum


def test(f, nums, max_sum):
    print(nums, max_sum)
    ms = f(nums)
    assert ms == max_sum, f'Expected: {max_sum}, actual: {ms}'
    print('Passed')


if __name__ == '__main__':
    test(max_subarray, [0], 0)
    test(max_subarray, [1, 2, 3], 6)
    test(max_subarray, [1, 2, -9, 3, 4], 7)
    test(max_subarray, [4, 2, -9, 3, 2], 6)
    # todo fix testcase
    test(max_subarray, [-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
