class Stack(object):

    def __init__(self, limit = 10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        if self.stk:
            return len(self.stk)
        else:
            print ("Stack is Empty")
            return None
            
    

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

