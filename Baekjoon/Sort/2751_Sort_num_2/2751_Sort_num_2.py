import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
num_ls = []
for n in range(N):
    num_ls.append(int(sys.stdin.readline()))

num_ls = list(set(num_ls))
num_ls.sort()
for i in range(len(num_ls)):
    print(num_ls[i])