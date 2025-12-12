import time
from dataclasses import dataclass
from typing import Optional, List, Any, Dict
def string_hash(s: str) -> int:
    h = 0
    p = 53
    mod = 2**64
    for ch in s:
        h = (h * p + ord(ch)) % mod
    return h


@dataclass
class Pair:
    key: str
    value: Any


class HashTable:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def _index(self, key: str):
        return string_hash(key) % self.capacity

    def put(self, key: str, value: Any):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for pair in bucket:
            if pair.key == key:
                pair.value = value
                return
        bucket.append(Pair(key, value))
        self.size += 1

    def get(self, key: str):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for pair in bucket:
            if pair.key == key:
                return pair.value
        return None

    def remove(self, key: str):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, pair in enumerate(bucket):
            if pair.key == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def visualize(self):
        return [[(pair.key, pair.value) for pair in bucket] for bucket in self.buckets]



ht = HashTable(8)
words = ["apple", "banana", "orange", "peach", "grape", "melon", "berry", "apple"]
for w in words:
    ht.put(w, ht.get(w) or 0)
    ht.put(w, ht.get(w) + 1)

print("=== HashTable visualization ===")
for i, bucket in enumerate(ht.visualize()):
    print(i, bucket)
