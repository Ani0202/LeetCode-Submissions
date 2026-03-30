# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        end_node = dummy
        prev = None
        i = 1
        while i < n:
            end_node = end_node.next
            i += 1

        while end_node.next:
            prev = curr
            curr = curr.next
            end_node = end_node.next

        prev.next = curr.next
        return dummy.next
