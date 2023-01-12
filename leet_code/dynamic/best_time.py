# not correct
from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = min(prices)
    ind_min = prices.index(min_price)
    max_price = max(prices[ind_min:])
    return max_price - min_price


def mp_dyn(prices: List[int]) -> int:
    pmin, pmax = prices[:2]
    prof_max = pmax - pmin
    return max(prof_max, 0)


def test(f, prices, profit):
    print(prices)
    mp = f(prices)
    assert profit == mp, f'Expected:  {profit}, actual: {mp}'
    print('Passed')


if __name__ == '__main__':
    test(max_profit, [3, 2, 1],                 0)
    test(max_profit, [1, 2, 3, 1, 5, 7, 1],     6)
    # todo fix it
    test(max_profit, [2, 4, 1],                 2)
