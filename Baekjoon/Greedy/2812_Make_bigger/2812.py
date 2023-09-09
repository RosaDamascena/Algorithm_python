import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = input().rstrip()
stack = []
for number in numbers:
    while stack and stack[-1] < number and K > 0:
        stack.pop()
        K -= 1
    stack.append(number)

if K > 0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))