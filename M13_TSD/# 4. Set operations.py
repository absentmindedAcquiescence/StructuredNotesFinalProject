# 4. Set operations
# Difficulty: Intermediate 
print("Input item count for list 1:", end=" ")
icount = int(input())

print("Input items for list 1:", end=" ")
list1 = [int(input()) for _ in range(icount)]

print("Input item count for list 2:", end=" ")
iicount = int(input())

print("Input items for list 2:", end=" ")
list2 = [int(input()) for _ in range(icount)]

set1 = set(list1)
set2 = set(list2)

print(f"Union of sets 1 and 2: {set1 | set2}")
print(f"Common items between sets 1 and 2: {set1 & set2}")
print(f"Unique items of set 1: {set1 - set2}")
print(f"Unique items of set 2: {set2 - set1}")
