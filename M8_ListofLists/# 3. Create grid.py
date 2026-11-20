# 3. Create a grid:
print("Input row and column length:", end=" ")

r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

print("Output:")
print(grid)