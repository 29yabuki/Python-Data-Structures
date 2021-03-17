class Queue():
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return self.items

if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())
    q.enqueue(4)
    q.enqueue('dog')
    q.enequeue(True)
    print(q)
    print(q.size())
    q.enqueue(8.4)
    q.dequeue()
    q.dequeue()
    print(q)
    print(q.size())