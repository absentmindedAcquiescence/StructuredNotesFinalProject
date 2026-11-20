# 5. Create a multiplication grid:
print("Input number:", end=" ")
n = int(input())

for i in range(1, n + 1):
    grid = []
    for j in range(1, n + 1):
        grid.append(i * j)
    print(*grid)