from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        # Visual:
        # Initially:
        # prev = None
        # curr -> [1] -> [2] -> [3] -> None

        while curr:
            temp = curr.next
            # temp stores the next node so we don't lose track:
            # temp -> curr.next
            # Example: if curr is [1], temp -> [2]

            curr.next = prev
            # Reverse pointer:
            # The current node now points backward to prev instead of forward to next.
            # If prev is None (first iteration), curr.next = None (new tail)

            prev = curr
            # Move prev forward to current node:
            # prev now marks the head of the reversed sublist

            curr = temp
            # Move curr forward to the next original node to process.

            # After first iteration example:
            # prev -> [1] -> None
            # curr -> [2] -> [3] -> None

        # When loop finishes, prev points to new head of reversed list:
        # e.g. [3] -> [2] -> [1] -> None

        return prev
