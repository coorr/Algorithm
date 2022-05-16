import sys
sys.stdin=open("5월/스택 2개로 큐 만들기/input.txt","r")

class Stack:
    def __init__(self):
        self.stack=[]
    def __repr__(self):
        return f"{self.stack}"
    def empty(self):
        if len(self.stack) == 0: 
            return True
        else: return False
    def push(self, item):
        return self.stack.append(item)
    def pop(self):
        return self.stack.pop()
st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.pop()

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def __repr__(self):
        return f"{self.stack1}"
    def push(self, item):
        self.stack1.append(item)
    def pop(self):
        self.peek()
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        result = self.stack2.pop()
        
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())     
                
        return result
    def empty(self):
        return not self.stack1 and not self.stack2
    
qu = Queue()
qu.push(1)
qu.push(2)
qu.push(3)

qu.pop()
print(qu)
    

        



    
    
    
    


