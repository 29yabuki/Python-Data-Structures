class Deque():
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == 0
    
    def add_front(self, item):
        self.items.append(item)
        
    def add_rear(self, item):
        self.items.insert(0, item)
        
    def remove_front(self):
        return self.items.pop()
        
    def remove_rear(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return self.items

if __name__ == '__main__':
    d = Deque()
    d.add_rear(4)
    d.add_rear('dogs')
    d.add_front('cats')
    d.add_front(True)
    print(d)
    print(d.size())
    d.add_rear(8.4)
    d.remove_rear()
    d.remove_front()
    print(d)