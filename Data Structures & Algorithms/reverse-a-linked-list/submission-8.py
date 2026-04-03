# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        stack = []
        curr = head
        while curr != None:
            stack.append(curr)
            curr = curr.next
        
        curr = stack.pop()
        head = curr
        while len(stack) > 0:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None

        return head
