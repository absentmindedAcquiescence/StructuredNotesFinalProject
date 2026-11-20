# 1. Building a list using .append()
print("Input item count:", end=" ")
icount = int(input())

print("Input items:", end=" ")
list = [input() for x in range(icount)]

print("List:", list)