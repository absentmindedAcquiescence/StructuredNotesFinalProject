# 6. Sorting and grabbing important values from a list
# using sorted(), min(), and max()
print("Input item count:", end=" ")
icount = int(input())

print("Input items:", end=" ")
list = [int(input()) for x in range(icount)]

print("Original list:", list)
print("Fixed list:", sorted(list))
print("Largest item:", max(list))
print("Smallest item:", min(list))