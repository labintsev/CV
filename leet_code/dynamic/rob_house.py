from typing import List


def robber(houses: List[int]) -> int:
    def max_profit(l, r):
        if r < l:
            return 0
        elif r == l:
            profit = houses[r]
        else:
            profit = max(houses[l:r+1])
        idx = houses.index(profit)
        profit += max_profit(l, idx-2)
        profit += max_profit(idx+2, r)
        return profit
    return max_profit(0, len(houses)-1)


def test(f, houses, expected):
    print(houses)
    actual = f(houses)
    assert actual == expected, f'Actual: {actual}, expected: {expected}'
    print('Passed')


if __name__ == '__main__':
    test(robber, [1], 1)
    test(robber, [1, 2, 3, 4], 6)
    test(robber, [10, 2, 3, 4], 14)
    test(robber, [10, 2, 8, 4], 18)
    # todo fix it
    test(robber, [0, 0, 0], 0)
