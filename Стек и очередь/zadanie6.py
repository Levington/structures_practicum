from dataclasses import dataclass
from typing import Any, Optional, List
import time

from zadanie5 import StackArray
class QueueCircularArray:

    def __init__(self, capacity=8):
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            raise OverflowError("Queue is full")
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("dequeue from empty queue")
        value = self.data[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def empty(self):
        return self.size == 0


class QueueTwoStacks:

    def __init__(self):
        self.s1 = StackArray() 
        self.s2 = StackArray()  

    def enqueue(self, value):
        self.s1.push(value)

    def dequeue(self):
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.push(self.s1.pop())
        if self.s2.empty():
            raise IndexError("dequeue from empty queue")
        return self.s2.pop()

    def empty(self):
        return self.s1.empty() and self.s2.empty()