class Stack():
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return self.items

class ReversedStack():
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.insert(0, item)
    
    def pop(self):
        self.items.pop(0)
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len( self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return self.items

if __name__ == '__main__':
    s = Stack()
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s)
    print(s.size())