class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.count = -1

    def append(self, item):
       
        if len(self.storage) == self.capacity:
            if (self.count + 1) == self.capacity:
                self.count = 0
            else:
                self.count += 1
            self.storage.pop(self.count)
            self.storage.insert(self.count, item)
                
        else:
            self.storage.append(item)

    def get(self):
        return self.storage