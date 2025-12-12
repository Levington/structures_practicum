class MinHeap:
    def __init__(self):
        self.heap = []
    
    def _sift_up(self, i):
        while i > 0 and self.heap[(i-1)//2] > self.heap[i]:
            self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1)//2
    
    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left, right = 2*i+1, 2*i+2
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
    
    def insert(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)
    
    def extract_min(self):
        if not self.heap:
            raise IndexError("Куча пуста")
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return min_val
    
    def build_heap(self, arr):
        self.heap = arr.copy()
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self._sift_down(i)
    
    def is_valid(self):
        for i in range(len(self.heap)):
            left, right = 2*i+1, 2*i+2
            if left < len(self.heap) and self.heap[i] > self.heap[left]:
                return False
            if right < len(self.heap) and self.heap[i] > self.heap[right]:
                return False
        return True


if __name__ == "__main__":
    print("=== Бинарная мин-куча ===\n")
    

    print("1. Вставка элементов:")
    h = MinHeap()
    for x in [5, 3, 8, 1, 2]:
        h.insert(x)
        print(f"   Вставка {x}: {h.heap}, корректно: {h.is_valid()}")
    

    print("\n2. Извлечение минимума:")
    for _ in range(3):
        m = h.extract_min()
        print(f"   Извлечён {m}: {h.heap}, корректно: {h.is_valid()}")
    
    print("\n3. Построение из массива:")
    h2 = MinHeap()
    arr = [9, 5, 6, 2, 3]
    print(f"   Исходный: {arr}")
    h2.build_heap(arr)
    print(f"   Куча: {h2.heap}, корректно: {h2.is_valid()}")
