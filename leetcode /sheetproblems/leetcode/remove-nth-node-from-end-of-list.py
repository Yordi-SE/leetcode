# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        second = dummy
        
        first = dummy
        while second.next != None:
            if n <= 0:
                first = first.next
            second = second.next
            if n > 0:
                n -= 1
            # print(n)
            # print("f",first)
            # print("s",second)
            # print("==========================")
        first.next = first.next.next

        return dummy.next