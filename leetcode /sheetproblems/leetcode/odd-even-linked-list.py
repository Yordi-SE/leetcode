# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        odd = head
        even = head.next
        head1 = head.next

        while (odd and odd.next) or (even and even.next):
            if odd and odd.next:
                odd.next = odd.next.next
                prev = odd
                odd = odd.next
            if even and even.next:
                even.next = even.next.next
                even = even.next
        if odd == None:
            prev.next = head1
        else:
            odd.next = head1
        return head