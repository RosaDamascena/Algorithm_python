i = '303CF3F3FCC0CF3F3CCFF303CFF3'
print(i)

# l = (len(bin_code) // 56) + 1   # 배율
# bin_code = bin_code.zfill(56*(l))
# bin_code = bin_code[::l]

A = bin(int(i, base=16))[2:].rstrip('0')   #.zfill(56)
if len(A) < 56:
    A_re = A.zfill(56)
elif 56 < len(A) < 112 :
    A_re = A.zfill(112)
elif 112 < len(A) < 280:
    A_re =A.zfill(280)
print(A_re)


check = '000000000000000000000000000303CF3F3FCC0CF3F3CCFF303CFF30000000000000000067F81E667F87861E187867E79E7E000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000799FE61E19E06781861E18799FE000000000000000000000'

A_ls = check.strip('0')
print(A_ls)