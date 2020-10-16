
class Stack():
    def __init__(self):
        self.items = [1,2,3,4,5]
    def enqueing(self,item):
        self.items.append(item)
        print(item)  
        a =self.items
        print(a)    
    def dequeing(self):
        b= self.items
        b.pop()
        print(b)
  

s=Stack()
print("Adding an element in the queue : ")
s.enqueing(6)
print("After removing an element from the queue : ")
s.dequeing()
