# 수업 내용 2 - 재귀 이진 탐색

def binary_search(arr, N, key, start, end) :
    while start <= end :
        mid = (start + end) // 2
        print(mid, arr[mid])
        if arr[mid] == key :
            return True
        elif arr[mid] > key :
            end = mid - 1
            binary_search(arr, N, key, start, end)
        else:
            start = mid + 1
            binary_search(arr, N, key, start, end)


numbers = list(range(1, 30, 2))
N = len(numbers)
target = 25

print(numbers)
print(binary_search(numbers, N, target, 0, N-1))