# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        n = 1
        last = head
        while last.next != None:
            n += 1
            last = last.next
        
        k = k % n
        if k == 0:
            return head
        
        last.next = head

        s = n - k
        t = head
        for _ in range(s - 1):
            t = t.next
        
        newhead = t.next
        t.next = None
        return newhead
