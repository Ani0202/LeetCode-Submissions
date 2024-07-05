# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        prev = None
        nextNode = head.next
        curr = head
        i = 0
        while nextNode:
            if prev != None:
                if (prev.val < curr.val and nextNode.val < curr.val) or (
                    prev.val > curr.val and nextNode.val > curr.val
                ):
                    arr.append(i)

            i += 1
            prev = curr
            curr = nextNode
            nextNode = nextNode.next

        if len(arr) < 2:
            return [-1, -1]
        return [min(arr[i + 1] - arr[i] for i in range(len(arr) - 1)), arr[-1] - arr[0]]
