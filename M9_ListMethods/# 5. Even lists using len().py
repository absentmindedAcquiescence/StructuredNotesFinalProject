# 5. Determining whether a list of items can be evenly
# split or not using len()
print("Input item count:", end=" ")
icount = int(input())

print("Input items:", end=" ")
list = [int(input()) for x in range(icount)]

print("List:", list)

if len(list) % 2 == 0:
    print("This list can be evenly split!")
else:
    print("This list cannot be evenly split!")