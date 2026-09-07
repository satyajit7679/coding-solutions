# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, times):
        prev = None
        curr = head

        while times > 0:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            times -= 1

        return prev, curr
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        left = head
        res = None
        prevleft = None

        while left:

            # Find the second node of the pair
            right = left

            for i in range((k - 1)):
                if right is None:
                    break
                right = right.next

            # Only one node remains
            if right is None:
                if prevleft:
                    prevleft.next = left
                break

            # Save node after the pair
            nextleft = right.next

            # Reverse the pair
            newhead, nextnode = self.reverse(left, k)

            # Connect previous part to reversed pair
            if prevleft:
                prevleft.next = newhead
            else:
                res = newhead

            # left is now the second node of the reversed pair
            prevleft = left

            # Move to next pair
            left = nextleft

        return res
        