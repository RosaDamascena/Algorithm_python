import heapq
arr = [6, 3, 2, 7, 9, 1]

heapq.heapify(arr)
print(arr)
heapq.heappush(arr, 5)
print(arr)
print(heapq.heappop(arr))