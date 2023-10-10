import sys
sys.stdin = open('input.txt')
import copy

t=int(input())
for qw in range(1,t+1):
    n,cnt=map(str,input().split())
    cnt=int(cnt)
    n=list(n)
    good= copy.deepcopy(n)
    good.sort(reverse=True)
    great=int(''.join(good))
    max_value=-1
    def back(depth,idx):
        global max_value
        if max_value==great:
            return
        if depth==cnt:
            value=int(''.join(n))
            max_value=max(max_value,value)
            return
        for j in range(idx,len(n)):
            for i in range(j+1,len(n)):
                if n[i] >=n[j]:
                    n[i],n[j]=n[j],n[i]
                    back(depth+1,j)
                    n[i],n[j]=n[j],n[i]
        if max_value==-1 :
            if cnt%2:
                n[-1],n[-2] = n[-2],n[-1]
            back(cnt,0)
    back(0,0)
    print(f'#{qw} {max_value}')