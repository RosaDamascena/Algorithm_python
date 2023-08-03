# 별찍기 - 7

'''
    *         4 -> 공백  1  -> 별
   ***        3         3
  *****       2         5
 *******      1         7  
*********     0         9
 *******      1         7
  *****       2         5
   ***        3         3
    *         4         1

L = 2×N-1
N = 1  L = 1
N = 2  L = 3
N = 3  L = 5
N = 4  L = 7
N = 5  L = 9
    .
    .
    .
'''

n = int(input())
length = n * 2 - 1
s = 0   #  i <= n 일 때
star = '*'
space = ' '

for i in range(1, length + 1) :
    if (i <= n) :
        length_star = i * 2 - 1
        print(f'{((n - i) * space )+ (length_star * star)}')
    elif (i > n) :
        s = length - i + 1  # i <= n 일 때의 i와 같이 풀기
        length_starr = s * 2 - 1
        print(f'{((n - s) * space )+ (length_starr * star)}')

'''
n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))
    
'''
