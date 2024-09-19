from min_heap import MinHeap

def main():
    heap = MinHeap()

    # Build heap from an array
    arr = [5, 9, 3, 10, 4, 8, 1, 7]
    print("Building heap from array:", arr)
    heap.build_min_heap(arr)
    heap.print_heap()

    # Insert a new element
    print("\nInserting element 2 into heap.")
    heap.insert(2)
    heap.print_heap()

    # Peek the minimum element
    print("\nPeek the minimum element:", heap.peek_min())

    # Pop the minimum element
    print("\nPop the minimum element:", heap.pop_min())
    heap.print_heap()

    # Pop elements one by one until the heap is empty
    print("\nPopping all elements from the heap:")
    while not heap.is_empty():
        print("Popped:", heap.pop_min())
        heap.print_heap()

if __name__ == "__main__":
    main()
