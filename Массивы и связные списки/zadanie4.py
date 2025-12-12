from collections.abc import Iterator
import time
from typing import Any, Optional

from zadanie1 import StaticArray
from zadanie2 import DynamicArray
from zadanie3 import SinglyLinkedList


class DNode:
    def __init__(self, value: Any, prev: Optional['DNode'] = None, next: Optional['DNode'] = None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[DNode] = None
        self.tail: Optional[DNode] = None
        self.size = 0

    def add_back(self, value):
        node = DNode(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def insert_after(self, node: DNode, value):

        if node is None:
            raise ValueError("node cannot be None")
        new_node = DNode(value)
        new_node.prev = node
        new_node.next = node.next
        node.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node
        self.size += 1
        return new_node

    def remove_node(self, node: DNode):

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = node.next = None
        self.size -= 1
        return node.value

    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def to_list(self):
        return list(iter(self))

print("=== Тест StaticArray ===")
sa = StaticArray(10)
sa.pushBack(1)
sa.pushBack(2)
sa.pushFront(0)  # [0,1,2]
sa.insert(2, 99) # [0,1,99,2]
print("StaticArray:", sa.to_list(), "find(99) ->", sa.find(99))
sa.remove(2)
print("After remove:", sa.to_list())

print("\n=== Тест DynamicArray ===")
da = DynamicArray(2)
for x in [1,2,3,4,5]:
    da.pushBack(x)
da.pushFront(0)
da.insert(3, 99)
print("DynamicArray:", da.to_list(), "find(99) ->", da.find(99))
da.remove(3)
print("After remove:", da.to_list())

print("\n=== Тест SinglyLinkedList ===")
sll = SinglyLinkedList()
sll.add_back(1)
sll.add_back(2)
sll.add_front(0)
sll.add_back(3)
print("Singly:", sll.to_list(), "find(2) ->", sll.find(2).value if sll.find(2) else None)
sll.remove_by_value(2)
print("After remove 2:", sll.to_list())
sll.reverse_in_place()
print("After reverse:", sll.to_list())

print("\n=== Тест DoublyLinkedList ===")
dll = DoublyLinkedList()
for i in range(5):
    dll.add_back(i)
print("Doubly:", dll.to_list())
# insert after head
node_head = dll.head
dll.insert_after(node_head, 99)
print("After insert_after head:", dll.to_list())
# remove node without search (remove the node we just created)
node_to_remove = node_head.next 
dll.remove_node(node_to_remove)
print("After remove_node:", dll.to_list())


N = 100_000


sa_big = StaticArray(N)
t0 = time.perf_counter()
for i in range(N):
    sa_big.pushBack(i)
t1 = time.perf_counter()
time_static = t1 - t0

da_big = DynamicArray(4)
t0 = time.perf_counter()
for i in range(N):
    da_big.pushBack(i)
t1 = time.perf_counter()
time_dynamic = t1 - t0

print("\n=== Время вставки N={} элементов ===".format(N))
print(f"StaticArray (preallocated capacity {N}): {time_static:.6f} s")
print(f"DynamicArray (initial capacity 4, doubling): {time_dynamic:.6f} s")
print("Замечание: StaticArray при предварительном выделении не делает копирований; DynamicArray делает копирования при росте, но амортизированная сложность добавления O(1).")

complexities = """
Оценки трудоемкости (в терминах n = текущий размер/количество элементов):
StaticArray:
  pushBack: O(1) (при наличии места) — в статическом массиве без перераспределения.
  pushFront: O(n) — сдвиг всех элементов.
  insert(index): O(n) — сдвиг (в худшем случае).
  remove(index): O(n) — сдвиг.
  find(value): O(n) — линейный поиск.

DynamicArray (strategy ×2):
  pushBack: амортизированно O(1) (в худшем случае одной операции O(n) для ресайза).
  pushFront: O(n) — сдвиг всех элементов (плюс возможный ресайз O(n)).
  insert(index): O(n) — сдвиг (плюс возможный ресайз).
  remove(index): O(n) — сдвиг.
  find(value): O(n).

SinglyLinkedList:
  add_front: O(1).
  add_back: O(1) (при наличии tail), иначе O(n).
  remove_by_value: O(n) — требуется поиск предыдущего узла.
  find: O(n).
  reverse_in_place: O(n) время, O(1) доп. память.

DoublyLinkedList:
  insert_after(node): O(1).
  remove_node(node): O(1).
  итерация: O(n).
  поиск по значению: O(n).

Сравнение операций вставки/удаления массив vs список (обобщённо):
  - Вставка/удаление в середине массива: O(n) (из-за сдвига). В списке — O(1) если у вас есть указатель на место вставки/удаления, но поиск этого места по индексу/значению стоит O(n).
  - Вставка в начало: массив O(n) (сдвиг), одно- или двусвязный список O(1).
  - Вставка в конец: массив амортизированно O(1) (динамический массив), список O(1) при наличии tail.
  - Удаление по значению: оба O(n) в общем случае; но удаление узла по ссылке в двусвязном списке O(1), а в массиве требуется сдвиг O(n).
"""
print(complexities)