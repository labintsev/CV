"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.
"""
import time


def hamming_distance(x: int, y: int) -> int:
    count = 0
    for cx, cy in zip(f'{x:32b}'.replace(' ', '0'), f'{y:32b}'.replace(' ', '0')):
        if cx != cy:
            count += 1
    return count


def hamming_distance_2(x: int, y: int) -> int:
    return bin(x ^ y).count('1')


def test_case_1(f):
    assert hamming_distance(4, 1) == 2
    assert hamming_distance(1, 4) == 2
    assert hamming_distance(5, 1) == 1
    assert hamming_distance(15, 1) == 3
    print('Test case 1 accepted')


def test_case_2(f):
    t0 = time.time()
    _ = [f(x, y) for x in range(1000) for y in range(1000)]
    print('Test case 2 take: ', time.time() - t0, ' s')


if __name__ == '__main__':
    test_case_1(hamming_distance)
    test_case_2(hamming_distance)
