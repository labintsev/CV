"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int):
        if self.min is None:
            self.min = val
        if val < self.min:
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min:
            self.min = min(self.stack)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min


def test_case_1():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()       # return -3
    minStack.pop()
    minStack.top()          # return 0
    minStack.getMin()       # return -2


def test_case_2():
    ms = MinStack()
    ms.push(-1)
    ms.top()
    x = ms.getMin()
    assert x == -1


if __name__ == '__main__':
    test_case_1()
    test_case_2()
