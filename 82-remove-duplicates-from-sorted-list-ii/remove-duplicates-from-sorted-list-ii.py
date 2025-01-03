# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        curr = dummyHead
        prev = None
        while head:
            if (None if prev == None else prev.val) != head.val and (None if head.next == None else head.next.val) != head.val:
                curr.next = head
                curr = curr.next
            prev = head
            head = head.next

        curr.next = None
        return dummyHead.next

        