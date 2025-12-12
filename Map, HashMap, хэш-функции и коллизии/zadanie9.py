import time
from dataclasses import dataclass
from typing import Optional, List, Any, Dict

from zadanie8 import HashTable, string_hash
def build_freq_map(text: str, hash_func):
    class BadHashTable(HashTable):
        def _index(self, key: str):
            return 1 

    class GoodHashTable(HashTable):
        def _index(self, key: str):
            return hash_func(key) % self.capacity

    T = BadHashTable if hash_func is None else GoodHashTable
    ht = T(128)

    for word in text.split():
        old = ht.get(word) or 0
        ht.put(word, old + 1)
    return ht


sample_text = """
apple banana apple grape banana apple fruit banana peach peach peach apple
orange berry apple fruit melon berry berry banana
"""

t0 = time.perf_counter()
bad_map = build_freq_map(sample_text, None)
t1 = time.perf_counter()

t2 = time.perf_counter()
good_map = build_freq_map(sample_text, string_hash)
t3 = time.perf_counter()

def top10(ht: HashTable):
    all_items = []
    for bucket in ht.buckets:
        for pair in bucket:
            all_items.append((pair.key, pair.value))
    return sorted(all_items, key=lambda x: -x[1])[:10]

print("\n=== Частотный словарь ===")
print("Top-10:", top10(good_map))
print("Время плохой хэш-функции:", t1 - t0)
print("Время хорошей хэш-функции:", t3 - t2)
