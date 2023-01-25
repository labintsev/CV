"""
Given an integer numRows, return the first numRows of Pascal's triangle.
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
import time
from typing import List


def pascal_triangle(n: int) -> List[List[int]]:

    def next_line(line):
        next_l = [1] * (len(line) + 1)
        for i in range(1, len(line)):
            next_l[i] = line[i - 1] + line[i]
        return next_l

    out = []
    line = [1]
    for i in range(n):
        out.append(line)
        line = next_line(line)
    return out


def pascal_triangle_2(numRows: int):
    a = [[1]]
    for i in range(1, numRows):
        line = [x + y for x, y in zip([0] + a[i-1], a[i-1] + [0])]
        a.append(line)
    return a


def test_case_1(f):
    assert f(1) == [[1]]
    assert f(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def test_case_2(f):
    t0 = time.time()
    f(2000)
    print('test 2 take: ', time.time() - t0, ' s')


if __name__ == '__main__':
    test_case_1(pascal_triangle_2)
    test_case_2(pascal_triangle)
