from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = 4000000
    profit_max = 0
    for i, p in enumerate(prices):
        if p < min_price:
            min_price = p
        elif p - min_price > profit_max:
            profit_max = p - min_price

    return profit_max


def mp_broot_force(prices: List[int]) -> int:
    prof_max = 0
    for i, pmin in enumerate(prices):
        for p_ in prices[i:]:
            prof = p_ - pmin
            prof_max = max(prof, prof_max)

    return max(prof_max, 0)


def test(f, prices, profit):
    print(prices)
    mp = f(prices)
    assert profit == mp, f'Expected:  {profit}, actual: {mp}'
    print('Passed')


if __name__ == '__main__':
    test(max_profit, [3, 2, 1],                 0)
    test(max_profit, [1, 2, 3, 1, 5, 7, 1],     6)
    test(max_profit, [12, 18, 1, 3],            6)
