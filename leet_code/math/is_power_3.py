import math


def is_power_3(n: int) -> bool:
    if n <= 0:
        return False
    if abs(math.log(n) / math.log(3) % 1) < 1e-8:
        return True
    else:
        return False


def is_power_3_1(n: int) -> bool:
    return n > 0 and 1162261467 % n == 0


if __name__ == '__main__':
    for n in [3**x for x in range(1, 20)]:
        print(n, is_power_3_1(n))
