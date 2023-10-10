def count_grid_points_in_circle(N):
    count = 0
    for x in range(-N, N+1):
        for y in range(-N, N+1):
            if x**2 + y**2 <= N**2:
                count += 1
    return count

# 테스트
N = 10
result = count_grid_points_in_circle(N)
print("반지름이", N, "인 원 안에 포함되는 격자점의 개수:", result)