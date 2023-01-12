from collections import namedtuple


def str_str(haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
        return -1
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i
    return -1


def test_str_str():
    TestCase = namedtuple('TestCase', 'haystack needle output')

    test_data = [
        TestCase('leetcode', 'leeto', -1),
        TestCase('sadbutsad', 'sad', 0),
        TestCase('sad', 'sadbutsad', -1),
        TestCase('sad', 'sad', 0),
    ]

    for tc in test_data:
        out = str_str(tc.haystack, tc.needle)
        assert out == tc.output, f'{tc}, Your: {out}'
        print(tc, ' - passed')


if __name__ == '__main__':
    test_str_str()
