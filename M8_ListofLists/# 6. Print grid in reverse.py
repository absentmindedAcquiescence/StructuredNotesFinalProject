# 6. Print a grid in reverse:
print("Input row and column length:", end=" ")

r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

reversedgrid = grid[::-1]

print("Output:")
for row in reversedgrid:
    print(" ".join(str(x) for x in row))