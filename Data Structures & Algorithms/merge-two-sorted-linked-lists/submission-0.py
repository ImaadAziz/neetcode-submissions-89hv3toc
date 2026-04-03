# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1 is None and list2 is None:
            return None
        p1 = list1
        p2 = list2
        if p1.val < p2.val:
            head = p1
            p1 = p1.next
        else:
            head = p2
            p2 = p2.next
        curr = head
        while p1 != None or p2 != None:
            if p1 == None:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
            elif p2 == None:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            elif p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            else:
                curr.next = p2
                p2 = p2.next
                curr = curr.next

        return head

