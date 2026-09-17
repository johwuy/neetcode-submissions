# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def pop(index):
            list_node = lists[index]
            if list_node is None:
                return None
            tmp = list_node.next
            list_node.next = None
            lists[index] = tmp
            return list_node

        min_value = float("-inf")
        dummy = ListNode()
        curr = dummy

        min_heap = []

        for i in range(len(lists)):
            node = pop(i)
            if node is None:
                continue
            heapq.heappush(min_heap, tuple([node.val, i]))

        while min_heap:
            smallest_val, index = heapq.heappop(min_heap)
            new_node = ListNode(smallest_val)
            curr.next = new_node
            curr = new_node
            if lists[index] is not None:
                node = pop(index)
                if node is None:
                    continue
                heapq.heappush(min_heap, tuple([node.val, index]))

        return dummy.next