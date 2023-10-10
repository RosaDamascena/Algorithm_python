# arr : 원본 배열
# N :  배열의 길이
# key : 타겟
def binary_search(arr, N, key) :
    start = 0
    end = N-1
    while start <= end :
        mid = (start + end) // 2
        print(mid, arr[mid])
        if arr[mid] == key :
            return True
        elif arr[mid] > key :
            end = mid - 1
        else:
            start = mid + 1

    return False

numbers = list(range(1, 30, 2))
N = len(numbers)
target = 25

print(numbers)
print(binary_search(numbers, N, target))
