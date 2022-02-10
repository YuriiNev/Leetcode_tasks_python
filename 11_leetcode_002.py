"""leetcode.com Task 2. Add Two Numbers.

You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example 1:_____

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:_____

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:_____

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""
# Definition for singly-linked list.
import typing as t


class ListNode:
    """Linked list definition."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Class for adding digits in two linked lists."""

    def addTwoNumbers(self,
                      l1: t.Optional[ListNode],
                      l2: t.Optional[ListNode]) -> t.Optional[ListNode]:
        """Add two linked lists and return the result."""
        rank = 0
        result = addTwoDigits(l1, l2, rk=rank)

        if result[0] is not None:
            res = ListNode(result[0])
            med = res
        else:
            return ListNode(0)
        rank = result[1]

        while result[1] is not None:
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            result = addTwoDigits(l1, l2, rk=rank)
            if result[0] is not None:
                med.next = ListNode(result[0])
                med = med.next
            elif rank != 0:
                med.next = ListNode(rank)
                med = med.next
                break
            else:
                break
            rank = result[1]

        # end while
        return res


def addTwoDigits(a: t.Optional[ListNode],
                 b: t.Optional[ListNode],
                 rk=0) -> t.Optional[tuple]:
    """Add two digits.

    a and b are digits, rk is a rank (0 or 1) from previous pair of digits
    returns (c,d); here c is the resulting digit and d is rank
    """
    if a is not None and b is not None:
        d = (a.val + b.val + rk) // 10
        c = a.val + b.val + rk - 10*d
        return (c, d)
    elif a is not None and b is None:
        d = (a.val + rk) // 10
        c = a.val + rk - 10*d
        return (c, d)
    elif b is not None and a is None:
        d = (b.val + rk) // 10
        c = b.val + rk - 10*d
        return (c, d)
    else:
        return (None, None)


l_1 = [9, 9, 9, 9, 9, 9, 9]
l_2 = [9, 9, 9, 9]

l1 = ListNode(l_1[0])
l2 = ListNode(l_2[0])

l1_temp = l1
l2_temp = l2

for i in range(1, len(l_1)):
    l1_temp.next = ListNode(l_1[i])
    l1_temp = l1_temp.next

for i in range(1, len(l_2)):
    l2_temp.next = ListNode(l_2[i])
    l2_temp = l2_temp.next

result = Solution.addTwoNumbers(Solution.addTwoNumbers, l1, l2)

k = 0
fp = []
while result is not None:
    fp.append(result.val)
    result = result.next
print(fp)
