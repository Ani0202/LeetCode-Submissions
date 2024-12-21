# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        shead = slow.next
        slow.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(shead)
        temp = ListNode()
        curr = temp
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next

        curr.next = head1 or head2

        return temp.next
