# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        evenHead = head.next
        prev = None
        nNode = None
        curr = head
        count = 0
        while curr.next:
            count = (count + 1) % 2
            nNode = curr.next
            prev = curr
            curr.next = curr.next.next
            curr = nNode

        if count == 1:
            prev.next = evenHead
        else:
            curr.next = evenHead

        return head
