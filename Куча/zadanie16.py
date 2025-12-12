class PriorityQueue:
    def __init__(self):
        self.heap = [] 
        self.counter = 0  
    
    def _sift_up(self, i):
        while i > 0 and self.heap[(i-1)//2][0] > self.heap[i][0]:
            self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1)//2
    
    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left, right = 2*i+1, 2*i+2
            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
    
    def push(self, value, priority):
        self.heap.append((priority, self.counter, value))
        self.counter += 1
        self._sift_up(len(self.heap) - 1)
    
    def pop(self):
        if not self.heap:
            raise IndexError("Очередь пуста")
        priority, _, value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return value, priority
    
    def peek(self):
        if not self.heap:
            raise IndexError("Очередь пуста")
        return self.heap[0][2], self.heap[0][0]
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def __len__(self):
        return len(self.heap)

def task_scheduling():
    print("=== Планирование задач ===\n")
    
    pq = PriorityQueue()
    
    tasks = [
        ("Отправить отчёт", 3),
        ("Исправить критический баг", 1),
        ("Обновить документацию", 5),
        ("Код-ревью", 2),
        ("Встреча с клиентом", 1),
        ("Рефакторинг", 4),
    ]
    
    print("Добавляем задачи:")
    for task, priority in tasks:
        pq.push(task, priority)
        print(f"  + '{task}' (приоритет: {priority})")
    
    print("\nВыполнение задач по приоритету:")
    step = 1
    while not pq.is_empty():
        task, priority = pq.pop()
        print(f"  {step}. [{priority}] {task}")
        step += 1
def find_k_smallest(arr, k):
    pq = PriorityQueue() 
    for x in arr:
        pq.push(x, x)
    result = []
    for _ in range(min(k, len(arr))):
        val, _ = pq.pop()
        result.append(val)
    
    return result


def demo_k_smallest():
    print("\n=== Поиск k минимальных элементов ===\n")
    
    arr = [64, 25, 12, 22, 11, 90, 45, 33, 7, 18]
    print(f"Массив: {arr}")
    
    for k in [3, 5]:
        result = find_k_smallest(arr, k)
        print(f"{k} минимальных: {result}")


if __name__ == "__main__":
    task_scheduling()
    demo_k_smallest()
