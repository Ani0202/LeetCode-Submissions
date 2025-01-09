# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        i = 1
        dummyNode = ListNode(0, head)
        prev = dummyNode
        curr = head
        while curr and i < left:
            prev = curr
            curr = curr.next
            i += 1

        tail = curr
        prevNode = None
        while curr and i <= right:
            temp = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = temp
            i += 1

        prev.next = prevNode
        tail.next = curr
        return dummyNode.next
