# 7. Sum of a grid:
print("Input row and column length:", end=" ")
r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

total = 0
for row in grid:
    for x in row:
        total += x 
print("Output:")
print(total)