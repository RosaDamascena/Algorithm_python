# 1620 - 나는야 포켓몬 마스터 이다솜
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
pokemon_dict = {}
for n in range(1, N + 1):
    a = sys.stdin.readline().strip()
    pokemon_dict[n] = a
    pokemon_dict[a] = n

for m in range(M):
    answer = sys.stdin.readline().strip()
    if answer.isdigit():
        print(pokemon_dict[int(answer)])
    else:
        print(pokemon_dict[answer])
