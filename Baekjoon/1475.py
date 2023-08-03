room_num = input()
set_num = [0] * 10
max_set = 0

for i in range(len(room_num)) :
    num = int(room_num[i])
    if num == 6 or num == 9 :
        if set_num[6] <= set_num[9] :
            set_num[6] += 1
        else : 
            set_num[9] += 1
    else :
        set_num[num] += 1

for i in range(len(set_num)) :
    if set_num[i] > max_set :
        max_set = set_num[i]

print(max_set)
