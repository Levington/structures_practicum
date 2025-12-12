from typing import Any, Optional


class SNode:
    def __init__(self, value: Any, next: Optional['SNode'] = None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[SNode] = None
        self.tail: Optional[SNode] = None
        self.size = 0

    def add_front(self, value):
        node = SNode(value, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def add_back(self, value):
        node = SNode(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove_by_value(self, value):
        prev = None
        cur = self.head
        while cur:
            if cur.value == value:
                if prev is None:
                    self.head = cur.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = cur.next
                    if prev.next is None:
                        self.tail = prev
                self.size -= 1
                return True
            prev = cur
            cur = cur.next
        return False

    def find(self, value):
        cur = self.head
        while cur:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def reverse_in_place(self):
        prev = None
        cur = self.head
        self.tail = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def to_list(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res