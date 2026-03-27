# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        k = len(lists)
        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        head = ListNode()
        curr = head
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

            curr = curr.next

        return head.next
