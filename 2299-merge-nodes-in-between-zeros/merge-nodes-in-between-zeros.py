# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modified = head
        curr = head.next
        while curr:
            if curr.val == 0:
                modified.next = None if curr.next is None else curr
                modified = modified.next
            else:
                modified.val += curr.val

            curr = curr.next

        return head
