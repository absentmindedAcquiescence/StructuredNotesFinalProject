# 2. Reordering lists using .index(), .insert() and .pop()
print("Input item count:", end=" ")
icount = int(input())

print("Input items:", end=" ")
list = [input() for x in range(icount)]

print("List:", list)

print("Input count target:", end=" ")
ctarget = input()
ctargetindex = list.index(ctarget)

print("Target index:", ctargetindex)
print("Input value to be inserted:", end=" ")
new = list.insert(ctargetindex, input())
list.pop()

print("Updated list:", list)