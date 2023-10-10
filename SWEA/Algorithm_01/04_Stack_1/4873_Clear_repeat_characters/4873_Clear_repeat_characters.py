# 4873 - 반복문자 지우기
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1) :
    string = input()
    stack = []      # 정답 문자열

    for s in string :   # 문자열 하나씩 비교
        if not stack :  # 스택이 비어 있으면
            stack.append(s)     # 문자열 stack에 넣어주기
        elif stack and stack[-1] != s :     # 스택에 값이 있고 top 값이 s가 아니라면
            stack.append(s)     # s를  스택에 넣어줌
        elif stack and stack[-1] == s :     # 스택에 값이 있고 top 값이 s라면
            stack.pop() # 연속 문자이므로 스택에서 없애줌

    if stack :
        print(f'#{t}', len(stack))
    else :
        print(print(f'#{t} 0'))
