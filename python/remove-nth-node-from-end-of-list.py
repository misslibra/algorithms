#!/usr/bin/env python3
# encoding: utf-8

# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
                """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        >>>
        """
        prev = head
        for i in range(n):
            prev = prev.next
        cursor = head

        if prev == None:
            return head.next

        while True:
            if prev.next:
                prev = prev.next
                cursor = cursor.next
            else:
                cursor.next = cursor.next.next
                break
        return head


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
