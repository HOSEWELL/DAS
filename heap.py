import heapq

heap = []

# Adding elements to heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 2)
heapq.heappush(heap, 15)

# Popping smallest element
print(heapq.heappop(heap))  
