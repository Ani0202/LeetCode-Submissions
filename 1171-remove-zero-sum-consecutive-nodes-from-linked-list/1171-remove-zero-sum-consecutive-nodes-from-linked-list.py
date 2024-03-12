# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        count = 0
        hmap = {}
        while curr is not None:
            count += curr.val
            if count in hmap:
                prev = hmap[count]
                curr = prev.next
                p = count + curr.val
                while p != count:
                    del hmap[p]
                    curr = curr.next
                    p += curr.val
                prev.next = curr.next
            else:
                hmap[count] = curr
            curr = curr.next

        return dummy.next  