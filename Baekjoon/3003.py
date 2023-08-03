# 킹, 퀸, 룩, 비숍, 나이트, 폰

T = list(map(int, input().split()))

set_chess = [1, 1, 2, 2, 2, 8]
add_piece = []

for i in range(len(T)) :
    if (T[i] > set_chess[i]) :
        add_piece.append((set_chess[i]-T[i]))
    elif (T[i] < set_chess[i]) :
        add_piece.append((set_chess[i]-T[i]))
    elif (T[i] == set_chess[i]) :
        add_piece.append(0)
    
print(*add_piece)