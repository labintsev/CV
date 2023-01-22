import time


def count_unopt(n: int) -> int:
    if n <= 2:
        primes = []
    elif n <= 3:
        primes = [2]
    elif n <= 5:
        primes = [2, 3]
    elif n <= 7:
        primes = [2, 3, 5]
    else:
        primes = [2, 3, 5, 7]

    nums = [x for x in range(9, n, 2) if not (x % 3 == 0 or x % 5 == 0 or x % 7 == 0)]
    for x in nums:
        is_prime = True
        for p in primes:
            if x % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return len(primes)


def count_primes(n: int) -> int:
    if n <= 2:
        return 0
    nums = [True] * n
    nums[0], nums[1] = False, False

    for i in range(2, n):
        if nums[i]:
            j = i ** 2
            while j < n:
                nums[j] = False
                j += i
    count = 0
    for x in nums:
        if x:
            count += 1
    return count


def test_case_2(power):
    t0 = time.time()
    count_primes(10 ** power)
    print(f'N = {power}', time.time() - t0, ' s')


def test_case_1():
    assert count_primes(0) == 0
    assert count_primes(1) == 0
    assert count_primes(2) == 0
    assert count_primes(3) == 1
    assert count_primes(10) == 4
    assert count_primes(100) == 25


if __name__ == '__main__':
    test_case_1()
    test_case_2(2)
    test_case_2(3)
    test_case_2(4)
    test_case_2(5)
    test_case_2(6)
