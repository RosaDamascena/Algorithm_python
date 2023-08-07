# 단어 공부

word_list = list(input().upper())
alphabet_num = {}

for i in word_list :
    if i in alphabet_num :
        alphabet_num[i] += 1
    else : 
        alphabet_num[i] = 1


#result = [k for k, v in alphabet_num.items() if max(alphabet_num.values()) == v]
result = []

for k, v in alphabet_num.items() :
    if max(alphabet_num.values()) == v :
        result.append(k)

if (len(result) > 1) :
    print('?')
else:
    print(*result)