from dataclasses import dataclass
from typing import Optional, List, Dict, Set, Tuple
from collections import deque
class TrieNode2:
    def __init__(self):
        self.children: Dict[str, TrieNode2] = {}
        self.is_word: bool = False
        self.prefix_count: int = 0 

class Trie2:
    def __init__(self):
        self.root = TrieNode2()

    def insert(self, word: str):
        node = self.root
        node.prefix_count += 1
        for ch in word:
            node = node.children.setdefault(ch, TrieNode2())
            node.prefix_count += 1
        node.is_word = True

    def count_prefix(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.prefix_count

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def delete(self, word: str) -> bool:
        path = []
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            path.append((node, ch))
            node = node.children[ch]
        if not node.is_word:
            return False
        node.is_word = False
        for parent, ch in reversed(path):
            child = parent.children[ch]
            child.prefix_count -= 1
            if child.prefix_count == 0:
                del parent.children[ch]
            else:
                break
        self.root.prefix_count -= 1
        return True