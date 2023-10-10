# 1234 - [S/W 문제해결 기본] 10일차 - 비밀번호
import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    n, s = map(str, input().split())
    password = False
    result = list(s)

    while password == False:
         for i in range(1, len(result)) :
            cnt = 0
            if result[i] == result[i-1] :
                result.pop(i-1)
                result.pop(i-1)
                cnt += 1
                break
         if cnt == 0:
            password = True


    print(f'#{t}', ''.join(result))