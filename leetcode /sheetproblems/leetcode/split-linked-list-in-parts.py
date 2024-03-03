# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        pointer = head
        counter = 0
        while pointer:
            counter += 1
            pointer = pointer.next
        pointer = head
        res = []
        part = counter//k
        parts = [part] * k
        l = 0
        for i in range(counter%k):
            parts[i] += (1)
        # print(parts)
        while pointer:
            if res:
                if len(res[-1]) == parts[l]:
                    res.append([ListNode(pointer.val)])
                    l += 1
                else:
                    res[-1].append(ListNode(pointer.val))
            else:
                res.append([ListNode(pointer.val)])
            pointer = pointer.next
        # print(part)
        for i in range(len(res)):
            for j in range(len(res[i])-1):
                res[i][j].next = res[i][j+1]
            res[i] = res[i][0]
        while len(res) < k:
            res.append(None)
        return res