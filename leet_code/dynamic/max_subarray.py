from typing import List


def max_subarray(nums: List[int]) -> int:
    n = len(nums)
    best_sum = total_sum = sum(nums)

    for left in range(0, n):
        if total_sum > best_sum:
            best_sum = total_sum
        cur_sum = total_sum
        for right in range(n-1, left, -1):
            cur_sum -= nums[right]
            if cur_sum > best_sum:
                best_sum = cur_sum

        total_sum -= nums[left]
    return best_sum


def maxSubArray(nums: List[int]) -> int:
    best_sum = - 10**4
    cur_sum = - 10**4
    for x in nums:
        if cur_sum <= 0:
            cur_sum = x
        else:
            cur_sum += x
        if cur_sum > best_sum:
            best_sum = cur_sum

    return best_sum


def test(f, nums, max_sum):
    print(nums, max_sum)
    ms = f(nums)
    assert ms == max_sum, f'Expected: {max_sum}, actual: {ms}'
    print('Passed')


if __name__ == '__main__':
    # todo fix testcase
    f = maxSubArray
    test(f, [-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    test(f, [-1, -2, -3, 1, -4], 1)
    test(f, [-1, -2, -3, -1, -4], -1)
    test(f, [-2, 1], 1)
    test(f, [0], 0)
    test(f, [1, 2, -9, 3, 4], 7)
    test(f, [1, 2, 3], 6)
    test(f, [4, 2, -9, 3, 2], 6)
    test(f, [-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
