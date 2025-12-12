from typing import Optional, List
from collections import deque


class BSTNode:
    def __init__(self, key: int, left: Optional['BSTNode'] = None, right: Optional['BSTNode'] = None):
        self.key = key
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: int):
        def _insert(node, key):
            if node is None:
                return BSTNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)

            return node
        self.root = _insert(self.root, key)

    def search(self, key: int) -> Optional[BSTNode]:
        node = self.root
        while node:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def delete(self, key: int):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, key):
            if node is None:
                return node
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:

                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = _min_value_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
            return node
        self.root = _delete(self.root, key)

    def inorder(self) -> List[int]:
        res = []
        def _in(node):
            if not node: return
            _in(node.left); res.append(node.key); _in(node.right)
        _in(self.root)
        return res

    def preorder(self) -> List[int]:
        res = []
        def _pre(node):
            if not node: return
            res.append(node.key); _pre(node.left); _pre(node.right)
        _pre(self.root)
        return res

    def postorder(self) -> List[int]:
        res = []
        def _post(node):
            if not node: return
            _post(node.left); _post(node.right); res.append(node.key)
        _post(self.root)
        return res

    def is_balanced(self) -> bool:
        def _check(node):
            if node is None:
                return 0, True
            lh, lb = _check(node.left)
            rh, rb = _check(node.right)
            h = max(lh, rh) + 1
            balanced = lb and rb and abs(lh - rh) <= 1
            return h, balanced
        return _check(self.root)[1]