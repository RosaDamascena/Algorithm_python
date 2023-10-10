# 4880 - Tournament Card Game
import sys
sys.stdin = open('input.txt')

def Game(F, B) :
    if member[F] == member[B] :
        return F
    else :
        if member[F] == 1 :
            if member[B] == 2 :
                return B
            elif member[B] == 3 :
                return F
        elif member[F] == 2 :
            if member[B] == 1 :
                return F
            elif member[B] == 3 :
                return B
        elif member[F] == 3 :
            if member[B] == 1 :
                return B
            elif member[B] == 2 :
                return F

def Division(start, end) :
    if start == end :
        return start
    Forth = Division(start, (start + end)//2)
    Back = Division((start + end)//2 + 1, end)

    return Game(Forth, Back)

T = int(input())
for t in range(1, T+1) :
    N = int(input())
    member = [0] + list(map(int, input().split()))
    start = 1
    end = N

    print(f'#{t}', Division(start, end))