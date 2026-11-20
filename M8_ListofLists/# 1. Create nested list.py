# 1. Create a nested list:
print("Input List 1 item count:", end=" ")
icount = int(input())

print("Input List 1 items:", end=" ")
list = [
    [str(input())] for _ in range(icount)
]

print("Output:")
print(list)