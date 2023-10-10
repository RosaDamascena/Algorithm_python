import sys
sys.stdin = open('input.txt')

n_list = [2, 3, 5, 7, 11]

T = int(input())

for t in range(1, T+1) :
    number = int(input())
    prime_fac = [0]*5
    for n in range(5) :
        while number % n_list[n] == 0 :
            number //= n_list[n]
            prime_fac[n] += 1

    print(f'#{t}', *prime_fac)
