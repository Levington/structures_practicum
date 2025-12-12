"""
Задание 10: Trie (префиксное дерево) с автодополнением
"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, 'TrieNode'] = {}
        self.end = False
        self.freq = 0  


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, freq=1):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True
        node.freq += freq

    def _collect(self, node: TrieNode, prefix: str, out: list):
        if node.end:
            out.append((prefix, node.freq))
        for ch, nxt in node.children.items():
            self._collect(nxt, prefix + ch, out)

    def autocomplete(self, prefix: str):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        result = []
        self._collect(node, prefix, result)
        return sorted(result, key=lambda x: -x[1])


sample_text = "apple banana apple peach berry apple banana peach fruit banana apple berry fruit peach berry apple banana"

text_words = sample_text.split()
freq_table = {}
for w in text_words:
    freq_table[w] = freq_table.get(w, 0) + 1

trie = Trie()
for w, f in freq_table.items():
    trie.insert(w, f)

print("=== Trie autocomplete ===")
print("prefix='b' :", trie.autocomplete("b"))
print("prefix='pe' :", trie.autocomplete("pe"))
print("prefix='ap' :", trie.autocomplete("ap"))