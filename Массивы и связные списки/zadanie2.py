class DynamicArray:
    def __init__(self, initial_capacity=4):
        self._capacity = max(1, initial_capacity)
        self._data = [None] * self._capacity
        self._size = 0

    def __len__(self):
        return self._size

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def pushBack(self, value):
        if self._size >= self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def pushFront(self, value):
        if self._size >= self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, 0, -1):
            self._data[i] = self._data[i-1]
        self._data[0] = value
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if self._size >= self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i-1]
        self._data[index] = value
        self._size += 1

    def remove(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        value = self._data[index]
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i+1]
        self._data[self._size-1] = None
        self._size -= 1
        return value

    def find(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1

    def to_list(self):
        return self._data[:self._size]