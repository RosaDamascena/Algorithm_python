# 크로아티아 알파벳
#from collections import Counter

croatia = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
word_length = len(word)
count_alpha = 0

for i in range(len(croatia)) :  # 'dz=' 가 한 자리가 더 많기 때문에 나눌 필요가 없었다...
    if(i == 2) :
        if(word.count(croatia[2]) > 0) :
            count_alpha += word.count(croatia[i])
    elif(i != 2) :
        count_alpha += (word.count(croatia[i]))

print(word_length - count_alpha)