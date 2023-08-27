# 2605 - 줄 세우기
import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = [0] + list(map(int, input().split()))
students = [0]

for i in range(1, N + 1):
    students.insert(i-numbers[i], i)

students.pop(0)
print(*students)
