class MinHeap:
    def __init__(self):
        self.heap = []

    # Helper functions to get parent, left, and right child indices using bit manipulation
    def parent(self, index):
        return (index - 1) >> 1  # (index - 1) // 2
    
    def left(self, index):
        return (index << 1) + 1  # 2 * index + 1
    
    def right(self, index):
        return (index << 1) + 2  # 2 * index + 2

    # Build the min heap
    def build_min_heap(self, arr):
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    # Heapify down (used for build_min_heap and pop)
    def heapify_down(self, index):
        smallest = index
        left_child = self.left(index)
        right_child = self.right(index)

        # Check if the left child is smaller than the current node
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        # Check if the right child is smaller than the smallest found so far
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        # If the smallest is not the current node, swap and continue heapifying down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    # Heapify up (used for inserting new elements)
    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            # Swap with parent
            parent_idx = self.parent(index)
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            index = parent_idx

    # Insert a new element into the heap
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    # Pop the root (min element) from the heap
    def pop_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return min_value

    # Peek the minimum element (root) without removing it
    def peek_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    # Check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # Print the heap
    def print_heap(self):
        print("Heap:", self.heap)
