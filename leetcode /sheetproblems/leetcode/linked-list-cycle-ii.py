# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        Tortoise = head.next
        if head and head.next:
            Rabbit = head.next.next
        else:
            return None
        while Rabbit and Rabbit.next and  Rabbit != Tortoise:
            Rabbit = Rabbit.next.next
            Tortoise = Tortoise.next
        if Rabbit == None or Rabbit.next == None:
            return None
        Rabbit = head
        while Rabbit != Tortoise:
            Tortoise = Tortoise.next
            Rabbit = Rabbit.next
        return Rabbit
        
