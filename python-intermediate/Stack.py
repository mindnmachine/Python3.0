class Stack(object):

    def __init__(self, limit = 10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        if self.stk:
            return len(self.stk)
        else:
            print ("Stack is Empty")
            
    

    def peek(self):
        if len(self.stk) <= 0:
            print("Stack Underflow")
            return 0
        else:
            print("Peek: Top Element of the stack")
            return self.stk[-1]

    def push(self,item):
            if len(self.stk) >= self.limit:
                    print("Stack Overflow")
                    self.resize(); 
            else:
                    self.stk.append(item)
            print("Stack after Push \n", self.stk)

    def pop(self):
            if len(self.stk) <= 0:
                    print("Stack Underflow")
                    return 0
            else:
                print("Pop: Top Element of the stack")
                return self.stk.pop()

    
    def size(self):
            return len(self.stk)    


    def resize(self):
        print("Resize:Doubling Stack size :\n")
        self.limit = 2*(self.limit)

my_stack = Stack(5)
my_stack.isEmpty()
my_stack.push("5")
my_stack.push("15")
my_stack.push("25")
print("Stack size is",my_stack.isEmpty())
my_stack.push("35")
my_stack.push("45")
my_stack.push("55")
my_stack.push("65")
my_stack.push("87")
my_stack.push("9")
my_stack.push("31")
my_stack.push("47")
my_stack.push("88")
my_stack.push("98")
my_stack.push("99")
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.peek())
