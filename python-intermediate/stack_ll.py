class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self,next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None

class Stack(object):
    def __init__(self,data=None):
        self.head= None
        if data:
            for data in data:
                self.push(data)

    def push(self,data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.getData()
        self.head = self.head.getNext()
        return temp

    def peek(self):
        if self.head is None:
           return None 
        return self.head.getData()

our_list = ["first","second","third","fourth"]
our_stack = Stack(our_list)

while(our_stack.peek() != None):
    print("Stack Value is ", our_stack.pop())

