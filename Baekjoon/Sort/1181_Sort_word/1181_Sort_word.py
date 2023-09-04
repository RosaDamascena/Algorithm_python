# 단어 정렬
import sys
sys.stdin = open('input.txt')

words_ls = []
N = int(sys.stdin.readline())
for n in range(N):
    words_ls.append(sys.stdin.readline().rstrip())

words_ls = list(set(words_ls))
words_ls.sort()
words_ls.sort(key=lambda x : (len(x)))

for i in range(len(words_ls)):
    print(words_ls[i])
