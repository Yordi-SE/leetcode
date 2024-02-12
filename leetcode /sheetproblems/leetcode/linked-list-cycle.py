# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(None, head)
        if head == None or head.next == None:
            return False
        Tortoise = head.next
        Rabbit = head.next.next

        while (Rabbit and Rabbit.next) and Tortoise != Rabbit:
            Rabbit = Rabbit.next.next
            Tortoise = Tortoise.next
        if Tortoise == Rabbit:
            return True
            # Rabbit = head
            # while Rabbit != Tortoise:
            #     Rabbit = Rabbit.next
            #     Tortoise = Tortoise.next
        return False
        
            