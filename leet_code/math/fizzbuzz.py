from typing import List


def fizzbuzz(n: int) -> List[str]:
    out = []
    for i in range(1, n+1):
        if i % 15 == 0:
            out.append('FizzBuzz')
            continue
        if i % 5 == 0:
            out.append('Buzz')
            continue
        if i % 3 == 0:
            out.append('Fizz')
            continue
        out.append(str(i))
    return out


def test_case_1():
    expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    actual = fizzbuzz(15)
    for e, a in zip(expected, actual):
        assert e == a


if __name__ == '__main__':
    test_case_1()
