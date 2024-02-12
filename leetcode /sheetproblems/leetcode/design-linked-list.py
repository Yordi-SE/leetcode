class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.total = 0

    def get(self, index: int) -> int:
        if self.total != 0 and (0 <= index < self.total):
            l = 1
            head = self.head
            while l <= index and head != None:
                head = head.next
                l += 1
            # print("getAt",index,"=>",head.val,self.linked(self.head))
            return head.val
            
        else:
            # print("getAt",index,"=>",self.linked(self.head))
            return -1
        
    def addAtHead(self, val: int) -> None:
        new_head = Node(val, self.head)
        self.head = new_head
        self.total += 1
        # print("AddAtHead","=>",self.linked(self.head))


    def addAtTail(self, val: int) -> None:
        dummy = Node(None, self.head)
        new_tail = Node(val, None)
        pointer = dummy
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = new_tail
        if self.head == None:
            self.head = new_tail
        self.total += 1
        # print("AddAtTail","=>",self.linked(self.head))
    def addAtIndex(self, index: int, val: int) -> None:
        if self.total != 0 and (0 <= index <= self.total):
            if index != 0:
                l = 1
                head = self.head
                prev = head
                while l <= index and head != None:
                    prev = head
                    head = head.next
                    l += 1
                new_node = Node(val, prev.next)
                prev.next = new_node
                self.total += 1
            else:
                self.addAtHead(val)
            # print("AddAtIndex",index,"=>",self.linked(self.head))
        elif self.total == 0 and index == 0:
            self.addAtHead(val)

    
    def deleteAtIndex(self, index: int) -> None:
        if self.total != 0 and (0 <= index < self.total):
            l = 1
            head = self.head
            prev = head
            while l <= index and head!= None:
                prev = head
                head = head.next
                l += 1
            prev.next = head.next
            if self.head == head:
                self.head = head.next
            self.total -= 1
        # print("delAtIndex",index,"=>",self.linked(self.head))
    def linked(self, head):
        pointer = head
        res = []
        while pointer != None:
            res.append(pointer.val)
            pointer = pointer.next
        return res


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)