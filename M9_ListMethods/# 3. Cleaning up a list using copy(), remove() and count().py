# 3. Cleaning up a list using .copy(), .remove() and .count()
print("Input item count:", end=" ")
icount = int(input())

print("Input items:", end=" ")
list = [input() for x in range(icount)]
altlist = list.copy()

print("Original list:", list)

print("Input count target:", end=" ")
ctarget = input()
total = list.count(ctarget)

for item in altlist:
    itotal = list.count(ctarget)
    if ctarget in list and itotal > 1:
        list.remove(ctarget)
    else:
        break

print("Count of duplicate items:", total)
print("Cleaned list:", list)
