from collections import namedtuple
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        out = f'[{self.val}, '
        while self.next:
            self = self.next
            out += f'{self.val}, '
        return out[:-2] + ']'


def linked_list(vals):
    head = ListNode()
    first = True
    curr = head
    for val in vals:
        if first:
            curr.val = val
            first = False
            continue
        else:
            new_node = ListNode()
            new_node.val = val
            curr.next = new_node
            curr = new_node
    return head


def equals(ll1: ListNode, ll2: ListNode) -> bool:
    while ll1:
        if ll1.val != ll2.val:
            return False
        ll1 = ll1.next
        ll2 = ll2.next
        if ll1 is None and ll2 is None:
            return True
        elif ll1 and ll2:
            continue
        else:
            return False


def test_equals():
    ll1 = linked_list([1, 2, 3])
    ll2 = linked_list([1, 2, 3, 4])
    print(equals(ll1, ll2))


def is_palindrome(head: Optional[ListNode]) -> bool:
    stack = []
    
    return False


TestCase = namedtuple('TestCase', 'head out')

test_data = [
    TestCase(linked_list([1, 2, 3, 4, 5]), False),
]

for tc in test_data:
    result = is_palindrome(tc.head)
    assert result == tc.out, f'Actual: {result}, expected: {tc.out}'
    print(tc, ' - passed')
