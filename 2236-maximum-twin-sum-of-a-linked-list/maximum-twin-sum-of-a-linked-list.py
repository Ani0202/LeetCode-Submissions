# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next

        fast = fast.next
        prev = slow
        curr = slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        fTwin = head
        lTwin = fast
        ans = 0
        while lTwin != slow:
            ans = max(ans, lTwin.val + fTwin.val)
            lTwin = lTwin.next
            fTwin = fTwin.next

        curr = fast
        prev = None
        while curr != slow:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return ans
