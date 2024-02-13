# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        dummy1 = ListNode(None,head)
        less = dummy
        greater = dummy1
        pointer = head
        while less and greater and pointer:
            if pointer.val < x:
                less.next = pointer
                less = less.next
            else:
                greater.next = pointer
                greater = greater.next
            pointer = pointer.next
        greater.next = None
        less.next = dummy1.next
        
        return dummy.next
        