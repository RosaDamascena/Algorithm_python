cal = '2+3*4/5'
# 최종 결과값
result = ''
stack = []

# 우선순위가 높은 순으로
for char in cal :
    if char in '+-*/()' :
        if char == '(' :
            stack.append(char)
        elif char in '*/' :
            while stack and stack[-1] in '*/' :
                result += stack.pop()
            stack.append(char)
        elif char in '+-' :
            while stack and stack[-1] != '(' :
                result += stack.pop()
            stack.append(char)
        elif char == ')' :
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

    else :
        result += char

while stack :
    result += stack.pop()

print(result)