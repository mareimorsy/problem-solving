# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while slow and fast:
            if fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
            if fast and slow and fast.val == slow.val:
                return True
        return False