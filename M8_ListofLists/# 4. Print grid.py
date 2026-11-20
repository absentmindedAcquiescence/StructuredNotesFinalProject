# 4. Print a grid:
print("Input row and column length:", end=" ")

r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

print("Output:")
for row in grid:
    print(" ".join(str(x) for x in row))