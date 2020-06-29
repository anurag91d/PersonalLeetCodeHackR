class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

    def reverselist(self):
        # print("inreverse")
        curr = self.head
        Num = int(0)
        reveredNum = int(0)
        while curr is not None:
            # print("cval: %d" %curr.get_data())
            Num = Num*10 + curr.get_data()
            # print("Num: %d" %Num)
            curr = curr.get_next()
        # print("Num: %d" %Num)
        while Num != 0:
            reveredNum = (Num % 10) + reveredNum*10
            # print("Num: %d" %Num)
            # print("reverN: %d" %reveredNum)
            Num = int(Num / 10)
        # print(reveredNum)
        return reveredNum


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        # print("In add")
        n1 = l1.reverselist()
        n2 = l2.reverselist()
        resultList = LinkedList(head=None)
        sum = n1 + n2
        # print(sum)
        sumrev =int(0)
        while sum != 0:
            sumrev = (sum % 10) + sumrev*10
            sum = int(sum / 10)
        # print(sumrev)
        while sumrev != 0:
            resultList.insert(sumrev % 10)
            sumrev = int(sumrev/10)
        return resultList


# create a linked list and insert some items
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
l1 = LinkedList(None)
l1.insert(3)
l1.insert(4)
l1.insert(2)
l2 = LinkedList(None)
l2.insert(4)
l2.insert(6)
l2.insert(5)
# l1.dump_list()
# l2.dump_list()
S1 = Solution()
r = S1.addTwoNumbers(l1, l2)
r.dump_list()
