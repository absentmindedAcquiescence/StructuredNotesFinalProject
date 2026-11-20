# 8. Transpose a grid
print("Input row and column length:", end=" ")
r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

for j in range(c):
    print(" ".join(str(grid[i][j]) for i in range(r)))  
