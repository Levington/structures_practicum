class StaticArray:
    def __init__(self, capacity: int):
        assert capacity >= 0
        self._data = [None] * capacity  
        self._capacity = capacity
        self._size = 0

    def __len__(self):
        return self._size

    def pushBack(self, value):
        if self._size >= self._capacity:
            raise OverflowError("StaticArray capacity exceeded")
        self._data[self._size] = value
        self._size += 1

    def pushFront(self, value):
        if self._size >= self._capacity:
            raise OverflowError("StaticArray capacity exceeded")
        for i in range(self._size, 0, -1):
            self._data[i] = self._data[i-1]
        self._data[0] = value
        self._size += 1

    def insert(self, index: int, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if self._size >= self._capacity:
            raise OverflowError("StaticArray capacity exceeded")
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i-1]
        self._data[index] = value
        self._size += 1

    def remove(self, index: int):
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
