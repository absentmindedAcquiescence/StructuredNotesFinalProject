# 2. Building a set using a list
# Difficulty: Easy
print("Input item count:", end=" ")
icount = int(input())

list = [int(input()) for _ in range(icount)]

print("Input count of items to append:", end=" ")
iicount = int(input())

for _ in range(iicount):
    list.append(int(input()))

set = set(list)

print("Original list:", end=" ")
print(*list, sep=", ")
print("Unique values:", end=" ")
print(*set, sep=", ")
