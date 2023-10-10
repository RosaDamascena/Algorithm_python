cal = '2+3*4/5'

result = ''
stack = []

#전수조사
for char in cal:
    if char not in '+-*/' :
        result += char
    else :
        stack.append(char)

while stack :
    result += stack.pop()