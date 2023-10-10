# 선택 정렬

def selection_sort(arr) :
    for i in range(len(arr)) :
        min_idx = i
        for j in range(i+1, len(arr)) :
            if arr[min_idx] > arr[j] :
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

numbers = [1, 45, 47, 5, 46, 4, 11, 76, 20, 33]
print(selection_sort(numbers))