from collections import namedtuple


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


def remove_nth(head, n):
    if not head.next:
        return ListNode()  # None
    p0 = None
    p1 = head
    p2 = head
    for _ in range(n):
        p2 = p2.next
    while p2:
        p0 = p1
        p1 = p1.next
        p2 = p2.next

    if p1.next:
        p1.val = p1.next.val
        p1.next = p1.next.next
    else:
        p0.next = None

    return head


TestCase = namedtuple('TestCase', 'head n out')

test_data = [
    TestCase(linked_list([1, 2, 3, 4, 5]), 1, linked_list([1, 2, 3, 4])),
    TestCase(linked_list([1, 2, 3, 4, 5]), 2, linked_list([1, 2, 3, 5])),
    TestCase(linked_list([1, 2]), 1, linked_list([1])),
    TestCase(linked_list([1, 2]), 2, linked_list([2])),
    TestCase(linked_list([1]), 1, linked_list([0])),
]

for tc in test_data:
    result = remove_nth(tc.head, tc.n)
    assert equals(result, tc.out), f'Actual: {tc.head}, expected: {tc.out}'
    print(tc, ' - passed')
