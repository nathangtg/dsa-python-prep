from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_list(self, node: Optional[ListNode]) -> None:
        """Helper to print linked list from node"""
        elements = []
        while node:
            elements.append(str(node.val))
            node = node.next
        print(" -> ".join(elements) + " -> None")

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        step = 0
        print("Initial list:")
        self.print_list(head)
        print("-" * 50)

        while curr:
            step += 1
            temp = curr.next  # Save next node

            print(f"Step {step} (Before Reversing Pointer):")
            print(f"  curr = {curr.val}")
            print(f"  temp = {temp.val if temp else None}")
            print(f"  prev = {prev.val if prev else None}")
            print("  List state:")
            print(f"   Reversed part (prev): ", end="")
            self.print_list(prev)
            print(f"   Remaining part (curr): ", end="")
            self.print_list(curr)
            print()

            curr.next = prev  # Reverse pointer

            print(f"Step {step} (After Reversing Pointer):")
            print(f"  curr = {curr.val} (now points to prev)")
            print(f"  curr.next = {curr.next.val if curr.next else None}")
            print()

            prev = curr  # Move prev forward
            curr = temp  # Move curr forward

            print(f"Step {step} (After Moving Pointers):")
            print(f"  prev = {prev.val}")
            print(f"  curr = {curr.val if curr else None}")
            print(f"  List state:")
            print(f"   Reversed part (prev): ", end="")
            self.print_list(prev)
            print(f"   Remaining part (curr): ", end="")
            self.print_list(curr)
            print("-" * 50)

        print("Final reversed list:")
        self.print_list(prev)
        return prev


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol = Solution()
sol.reverseList(head)
