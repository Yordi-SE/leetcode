# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        set1 = set()
        dummy = ListNode(None, head)
        prev = head
        current = head
        while current:
            if current.val in set1:
                prev.next = current.next
                current = prev.next
            else:
                set1.add(current.val)
                prev = current
                current = current.next
        return dummy.next