import time


def num_bits(n: int) -> int:
    count = 0
    for s in bin(n):
        if s == '1':
            count += 1
    return count


def num_bits_2(n: int) -> int:
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count


def num_bits_3(n: int) -> int:
    return bin(n).count('1')


def test_case_1(f):
    assert f(0) == 0
    assert f(1) == 1
    assert f(2) == 1
    assert f(3) == 2
    print('Test case 1 accepted')


def test_case_2(f):
    t0 = time.time()
    for n in range(10**6):
        f(n)
    print('Test case 2 accepted, take: ', time.time() - t0, ' s')


if __name__ == '__main__':
    test_case_1(num_bits_3)
    test_case_2(num_bits_3)
