def roman_to_int(s: str) -> int:
    d = dict(zip('IVXLCDM', (1, 5, 10, 50, 100, 500, 1000)))
    out = 0
    cur = 'I'
    for r in reversed(s):
        if d[r] > d[cur]:
            out += d[r]
            cur = r
        elif d[r] == d[cur]:
            out += d[r]
        else:
            out -= d[r]
    return out


def test_case_1():
    assert roman_to_int('I') == 1
    assert roman_to_int('VI') == 6
    assert roman_to_int('IV') == 4
    assert roman_to_int('IM') == 999
    assert roman_to_int('MDCLXVI') == 1666


if __name__ == '__main__':
    test_case_1()
