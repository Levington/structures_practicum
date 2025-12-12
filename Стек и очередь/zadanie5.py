from dataclasses import dataclass
from typing import Any, Optional, List
import time
class StackArray:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.data:
            raise IndexError("pop from empty stack")
        return self.data.pop()

    def peek(self):
        return self.data[-1] if self.data else None

    def empty(self):
        return len(self.data) == 0


@dataclass
class Node:
    value: Any
    next: Optional['Node'] = None

class StackLinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        self.head = Node(value, self.head)

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        val = self.head.value
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.value if self.head else None

    def empty(self):
        return self.head is None


def check_brackets(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    st = StackArray()
    for ch in s:
        if ch in "([{":
            st.push(ch)
        elif ch in ")]}":
            if st.empty() or st.pop() != pairs[ch]:
                return False
    return st.empty()