# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        prev, second_half_head = None, slow_ptr.next
        slow_ptr.next = None

        while second_half_head:
            tmp = second_half_head.next
            second_half_head.next = prev
            prev = second_half_head
            second_half_head = tmp

        h1 = head
        h2 = prev
        while h2:
            tmp = h1.next
            h1.next = h2
            h1 = h2
            h2 = tmp