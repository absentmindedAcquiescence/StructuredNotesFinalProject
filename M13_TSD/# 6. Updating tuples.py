# 6. Updating tuples + tuple memory using a list
# Difficulty: Intermediate
fulllist = []

print("Input items?")
print("1 - Yes")
print("2 - No")
choice = int(input())

while choice < 2:

    print("Input item count:", end=" ")
    icount = int(input())

    print("Input items:", end=" ")

    list = [input() for _ in range(icount)]
    tuple1 = tuple(list)

    fulllist.append(tuple1)

    list.clear()

    print("Input count of items to append:", end=" ")
    iicount = int(input())

    print("Input items:", end=" ")

    for _ in range(iicount):
        list.append(input())

    tuple2 = tuple(list)

    fulllist.append(tuple2)

    print("New tuple:", end=" ")
    print(*tuple2, sep=", ")
    print("Previous tuple:", end=" ")
    print(*tuple1, sep=", ")
    print("Full list:", sep=", ")
    print(*fulllist, sep=", ")

    print("Input items again?")
    print("1 - Yes")
    print("2 - No")
    choice = int(input())

print("Thank you for using!")