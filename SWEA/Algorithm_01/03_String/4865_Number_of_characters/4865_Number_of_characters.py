# 4865 - 글자수
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1) :
    str1 = set(input())
    # 중복 글자수가 있기 때문에 set을 사용하여 중복 글자 없애줌
    str2 = input()
    count_dict = {} # 글자 수 딕셔너리 생성
    max_c = 0

    for i in str1 :
        for j in str2 :
            if j == i : # str1의 i와 str2 j비교
                if j in count_dict :
                    count_dict[j] += 1
                else :
                    count_dict[j] = 1

    for v in count_dict.values() :
        if v > max_c :
            max_c = v

    print(f'#{t}', max_c)