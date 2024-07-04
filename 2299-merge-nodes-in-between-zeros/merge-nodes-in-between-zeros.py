# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head.next
        curr = temp
        while curr:
            tempSum = 0
            while curr.val != 0:
                tempSum += curr.val
                curr = curr.next

            temp.val = tempSum
            curr = curr.next
            temp.next = curr
            temp = temp.next
        return head.next
