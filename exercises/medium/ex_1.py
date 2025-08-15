class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.next = 0
        self.oldest = 0
        self.buffer = [None] * size

    def get(self):
        if self.next == self.oldest and self.buffer[self.oldest] == None:
            return None

        value = self.buffer[self.oldest]
        self.buffer[self.oldest] = None
        self.oldest = (self.oldest + 1) % self.size
        return value

    def put(self, value):
        if self.next == self.oldest and not self.buffer.count(None) == self.size:
            self.oldest = (self.oldest + 1) % self.size

        self.buffer[self.next] = value
        self.next = (self.next + 1) % self.size


buffer = CircularBuffer(3)

print(buffer.get() is None)  # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)  # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)  # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)  # True
print(buffer.get() == 6)  # True
print(buffer.get() == 7)  # True
print(buffer.get() is None)  # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)  # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)  # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)  # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)  # True
print(buffer2.get() == 5)  # True
print(buffer2.get() == 6)  # True
print(buffer2.get() == 7)  # True
print(buffer2.get() is None)  # True
