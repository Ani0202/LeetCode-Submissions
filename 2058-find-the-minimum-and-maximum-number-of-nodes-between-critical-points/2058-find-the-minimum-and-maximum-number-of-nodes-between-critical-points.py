# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        i = 1
        prev = None
        curr = head
        arr = []
        while curr:
            if prev and curr.next:
                if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                    arr.append(i)
            i += 1
            prev = curr
            curr = curr.next

        if len(arr) < 2:
            return [-1, -1]
        m = arr[1]-arr[0]
        for i in range(1, len(arr)):
            m = min(m, arr[i]- arr[i-1])

        return [m, arr[-1]-arr[0]]
        