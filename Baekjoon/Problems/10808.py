word = list(str(input()))
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num_alpha = []

for i in range(len(alpha_list)):
	num_al = word.count(alpha_list[i])
	num_alpha.append(num_al)
    
print(*num_alpha, end=' ')