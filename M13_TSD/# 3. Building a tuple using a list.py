# 3. Building a tuple using a list
# Difficulty: Easy
print("Input item count:", end=" ")
icount = int(input())

print("Input items:", end=" ")

list = [input() for _ in range(icount)]
tuple = tuple(list)

print("Input count of items to append:", end=" ")
iicount = int(input())

print("Input items:", end=" ")

for _ in range(iicount):
    list.append(input())

print("Modified list:", end=" ")
print(*list, sep=", ")
print("Original list:", end=" ")
print(*tuple, sep=", ")