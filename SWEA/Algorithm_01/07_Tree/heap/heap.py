# 최소힙 - 값 삽입 연산
N = 6
arr = [6, 3, 2, 7, 9, 1]

tree = [0] * (N+1) # 리스트의 길이가 주어지지 않을 때 빈 배열에 append
last = 1

for i in range(N):
    if tree[i] == 0:
        tree[last] = arr[i]
    else :
        last += 1
        tree[last] = arr[i]
        child = last
        parent = child // 2

        while parent >= 1 and tree[parent] > tree[child]:   # 최소힙
            # 부모, 자식 값 교환
            tree[parent], tree[child] = tree[child], tree[parent]
            # 자식의 위치가 swap한 부모의 위치가 되도록 설정
            child = parent
            # 부모의 값 재설정
            parent = child // 2

    print(tree)