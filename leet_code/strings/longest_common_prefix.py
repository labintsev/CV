"""
Find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

from collections import namedtuple
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    out = ''
    min_ls = 200
    for s in strs:
        if len(s) < min_ls:
            min_ls = len(s)

    for i in range(min_ls):
        ch = strs[0][i]
        for s in strs[1:]:
            if s[i] != ch:
                return out
        out += ch

    return out


def longest_common_prefix_2(strs: List[str]) -> str:
    match = 0
    for val in zip(*strs):
        if len(set(val)) == 1:
            match += 1
        else:
            break
    return strs[0][:match]


def test(f):
    TestCase = namedtuple('TestCase', 'strs out')
    test_data = [
        TestCase(["flower", "flow", "light"], ''),
        TestCase(["flower", "flow", ""], ''),
        TestCase(["flower", "flow", "flight"], 'fl'),
        TestCase(["flower"], 'flower'),
        TestCase([""], ''),
    ]
    for tc in test_data:
        out = f(tc.strs)
        assert out == tc.out, f'{tc}, yours: {out}'
        print(tc, ' passed')


def test_zip():
    strs = ["flower", "flow", "flight"]
    for val in zip(*strs):
        print(val)


if __name__ == '__main__':
    # test(longest_common_prefix_2)
    test_zip()
