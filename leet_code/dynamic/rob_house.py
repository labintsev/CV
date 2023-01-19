from typing import List


def robber_recursive(houses: List[int]) -> int:
    def max_profit(l, r):
        if r < l:
            return 0
        elif r == l:
            return houses[r]
        else:
            profit = max(houses[l:r+1])
        idx = houses.index(profit)
        profit += max_profit(l, idx-2)
        profit += max_profit(idx+2, r)
        return profit
    return max_profit(0, len(houses)-1)


def robber_iterative(houses: List[int]) -> int:
    can_rob = True
    profit = last_profit = 0

    for x in houses:
        if can_rob:
            last_profit = profit
            profit += x
            can_rob = False
        else:
            if x + last_profit > profit:
                profit, last_profit = last_profit + x, profit
            else:
                can_rob = True

    return profit


def test(f, houses, expected):
    print(houses)
    actual = f(houses)
    assert actual == expected, f'Actual: {actual}, expected: {expected}'
    print('Passed')


if __name__ == '__main__':
    f = robber_iterative
    test(f, [2, 3, 2], 4)
    test(f, [0, 0, 0], 0)
    test(f, [1], 1)
    test(f, [1, 2, 3, 4], 6)
    test(f, [10, 2, 3, 4], 14)
    test(f, [10, 2, 8, 4], 18)

