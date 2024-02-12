# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast  = fast.next.next
        middle = slow
        pointer = slow
        prev = slow
        
        while pointer:
            next = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = next
        slow.next = None
        pointer = prev
        first = head
        # print(prev)

        while pointer != middle:
            # print(pointer)
            # print("=====================")
            # print(first)
            if pointer.val != first.val:
                return False
            pointer = pointer.next
            first = first.next
        if pointer.val != first.val:
            return False
        return True
        