# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        first = head
        second = head
        rest1,rest2 = head,head
        for i in range(right):
            if rest1:
                rest1 = rest1.next
        for i in range(left-2):
            print(i)
            rest2 = rest2.next
        for i in range(right-1):
            first = first.next
        for i in range(left-1):
            second = second.next
        if rest2 != second:
            rest2.next = None
        if first:
            first.next = None
        pointer = second
        prev = None
        while pointer and pointer != first.next:
            next = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = next
        # print(first)
        second.next = rest1
        if rest2 != second:
            rest2.next = first
        else:
            return first
        return head
            
