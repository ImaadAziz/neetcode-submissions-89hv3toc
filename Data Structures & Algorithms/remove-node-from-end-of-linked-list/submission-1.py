# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = head
        stack = []
        while root:
            stack.append(root)
            root = root.next
        curr = None
        for i in range(n-1):
            curr = stack.pop()
        rem = stack.pop()
        if len(stack) != 0:
            prev = stack.pop()
            prev.next = curr
        else:
            return curr
        return head
