# 10816 - 숫자 카드2
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def Binary_Search(start, end, cards, c):
    if start > end:
        return 0
    mid = (start + end) // 2
    if c == cards[mid]:
        return cards[start: end + 1].count(c)
    elif c < cards[mid]:
        return Binary_Search(start, mid - 1, cards, c)
    else:
        return Binary_Search(mid + 1, end, cards, c)


N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
check = map(int, input().split())
answer = {}

for c in cards:
    start = 0
    end = N - 1
    if c not in answer:
        answer[c] = Binary_Search(start, end, cards, c)

for ch in check:
    if ch in answer:
        print(answer[ch], end=' ')
    else:
        print(0, end=' ')
