# 4866 - 괄호 검사
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    sentence = input()  # 문장 입력받기
    stack = []      # 빈 스택 만들기
    for i in sentence:  # 문장 한 글자씩 확인
        if i == '(' or i == '{':    # 둘 중에 하나라면 stack에 넣어주기(찾을 값)
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':  # 스택에 값이 있고 top의 값이 '('일때
                stack.pop()     # 짝이 맞으니까 stack에서 pop해주기!
            else:
                stack.append(0) # stack에 값이 없으면 안되니까 0넣어주기
                break       # 짝이 안 맞으니까 멈추기
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(0)
                break

    if not stack:
        print(f'#{t} 1')    # 스택이 비어있으면 성공 1 출력
    else:
        print(f'#{t} 0')    # 스택에 값이 남아있으면 실패 0 출력