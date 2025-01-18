import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        heap = []
        for i in range(k):
            if lists[i]:
                heap.append((lists[i].val, i, lists[i]))

        heapq.heapify(heap)
        dummyNode = ListNode()
        curr = dummyNode
        while heap:
            val, ind, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, ind, node.next))

        return dummyNode.next
