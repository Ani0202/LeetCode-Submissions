# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        dummyNode = ListNode(0, head)
        curr = head
        prev = dummyNode
        i = 0
        while i < n - 1:
            fast = fast.next
            i += 1

        while fast.next:
            fast = fast.next
            prev = curr
            curr = curr.next

        prev.next = prev.next.next
        return dummyNode.next
