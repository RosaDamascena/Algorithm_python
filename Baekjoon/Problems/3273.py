# 배열 - 두 수의 합

N = int(input())
num_list = list(map(int, input().split()))
sum_num = int(input())
sets = 0

for i in range(len(num_list)) :
    if ((sum_num - num_list[i]) in num_list) :
        sets += 1

print(int(sets/2))
