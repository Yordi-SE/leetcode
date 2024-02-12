# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        dummy = ListNode(None,None)
        curr = dummy
        second = list2
        while first or second:
            while second and first and first.val <= second.val:
                if curr == dummy:
                    curr.next = first
                    curr = curr.next
                else:
                    curr.next = first
                    curr = curr.next
                first = first.next
            if first and second == None:
                if curr == dummy:
                    curr.next = first
                    curr = curr.next
                else:
                    curr.next = first
                    curr = curr.next
                first = first.next
            if second and curr == dummy:
                curr.next = second
                curr = curr.next
            elif second:
                curr.next = second
                curr = curr.next
            if second:
                second = second.next
        return dummy.next
            