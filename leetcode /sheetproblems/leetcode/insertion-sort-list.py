# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = head
        stack = []
        # if head == None:
        #     return None
        # pointer = head.next
        # while pointer != None:
        #     next = pointer.next
        #     pointer.next = prev
        #     prev = pointer
        #     pointer = next
        # head.next = None
        # head = prev
        pointer = head
        while pointer:
            stack.append(pointer)
            pointer = pointer.next
        while stack:
            pointer = stack.pop()
            while pointer.next and pointer.val < pointer.next.val:
                pointer.val,pointer.next.val= pointer.next.val,pointer.val
                pointer = pointer.next
        prev = head
        stack = []
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
        pointer = head
        return head

