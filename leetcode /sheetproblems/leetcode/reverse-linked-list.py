# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if head == None:
            return None
        pointer = head.next
        while pointer != None:
            next = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = next
        head.next = None
        head = prev
        return head