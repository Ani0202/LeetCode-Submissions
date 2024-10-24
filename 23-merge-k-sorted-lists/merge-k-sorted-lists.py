# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        k = len(lists)
        head = ListNode()
        currNode = head
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            val, idx, curr = heapq.heappop(heap)
            temp = curr.next
            currNode.next = curr
            currNode = currNode.next
            if temp:
                heapq.heappush(heap, (temp.val, idx, temp))

        return head.next
