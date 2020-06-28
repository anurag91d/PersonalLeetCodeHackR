class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def addNode(self, Node):
        Node.next = self.head
        self.head = Node

    def printList(self):
        print("--- Linked List ---")
        printData = self.head
        while printData is not None:
            print(printData.val, end=" ---> ")
            printData = printData.next
        print("")

    def addAtPos(self, data, n):
        count = 0
        new = Node(data)
        i = self.head
        while i is not None:
            count +=1
            if count == n:
                new.next = i.next
                i.next = new
                self.printList()
                break
            else:
                i = i.next
        return "Position Not Found"

    def removeNodebyData(self,data):
        i = self.head
        prev = None
        if i.val == data:
            self.head = None
        while i is not None:
            if i.val == data:
                prev.next = i.next
                i.next = None
                self.printList()
                break
            else:
                prev = i
                i = i.next
        return "Data Not Found"
    def reverseList(self):
        c = self.head
        n = None
        p = None
        while c is not None:
                n = c.next
                c.next = p
                p = c
                c = n
        self.head = p
        self.printList()







nums = [0, 14, 26, 83, 99, 1244, 50, 2, 98, 111, 44, 5]
L1 = LinkedList()
for i in range(0,len(nums)):
    N = Node(nums[i])
    L1.addNode(N)
L1.printList()
L1.addAtPos(5555, 5)
L1.removeNodebyData(5555)
L1.reverseList()
# L1.addAtPos(5555,0)
# print(L1.addAtPos(5555,8))
# print(L1.addAtPos(5555,7))




