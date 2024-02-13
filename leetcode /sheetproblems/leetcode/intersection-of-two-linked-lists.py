# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        set1 = set()
        set2 = set()
        first = headA
        second = headB
        while True:
            if first == None and second == None:
                # print(set2)
                # print(set1)
                return None
            if first:
                set1.add(first)
                if first in set2:
                    # print(set2)
                    # print(set1)
                    return first
                first = first.next
            if second:
                set2.add(second)
                if second in set1:
                    # print(set2)
                    # print(set1)
                    return second
                second = second.next
        print(set1)
        
        