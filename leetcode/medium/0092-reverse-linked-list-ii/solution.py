# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return None

        if left == right:
            return head

        t = head
        before = None
        pos = 1

        # reach left position
        while pos < left:
            before = t
            t = t.next
            pos += 1

        curr = t
        prev = None

        times = right - left + 1

        # reverse
        while times:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            times -= 1

        # connect
        t.next = curr

        if before != None:
            before.next = prev
        else:
            head = prev

        return head