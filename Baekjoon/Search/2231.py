N = int(input())

answer = 0
for i in range(1, N):
    now = str(N - i)
    d = list(map(int, now.rstrip()))
    if sum(d) == i:
        answer = now

print(answer)