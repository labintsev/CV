"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
import time


def is_valid(s: str) -> bool:
    opens = '([{'
    stack = []
    for p in s:
        if p in opens:
            stack.append(p)
            continue
        else:
            if len(stack) == 0:
                return False
            else:
                pops = stack.pop(-1)
                if (pops == '(' and p == ')') or (pops == '[' and p == ']') or (pops == '{' and p == '}'):
                    continue
                else:
                    return False
    if len(stack) == 0:
        return True


def is_valid_2(s: str) -> bool:
    parts = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for p in s:
        if p in parts.keys():
            stack.append(p)
            continue
        else:
            if len(stack) == 0:
                return False
            else:
                pops = stack.pop(-1)
                if parts[pops] == p:
                    continue
                else:
                    return False
    if len(stack) == 0:
        return True


def test_case_1(f):
    assert f('()')
    assert f('()[]{}')
    assert not f(')(')
    assert not f('(]')


def test_case_2(f):
    t0 = time.time()
    f('()[]{}' * 1_000_000)
    print('test case 2 take: ', time.time() - t0, ' s')


if __name__ == '__main__':
    test_case_1(is_valid_2)
    test_case_2(is_valid_2)
