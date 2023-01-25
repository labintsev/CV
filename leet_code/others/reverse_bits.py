"""Reverse bits of a given 32 bits unsigned integer."""


def reverse_bits(n: int) -> int:
    s = f'{n:32b}'.replace(' ', '0')
    return int(s[::-1], 2)


def test_case_1(f):
    assert f(43_261_596) == 964_176_192
    assert f(4_294_967_293) == 3_221_225_471
    assert f(1) == 2147483648


if __name__ == '__main__':
    test_case_1(reverse_bits)
