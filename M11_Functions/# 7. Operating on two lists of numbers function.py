# 7. Two number operations using two lists
# Difficulty: Hard
print("Add numbers?")
print("1 - Yes")
print("2 - No")
choice = (int(input()))

def complexnumbers(list1, list2):
    newlist = []
    for item1 in list1:
        for item2 in list2:
            total = item1 + item2
            diff = item1 - item2
            prod = item1 * item2
            if item1 < 0 or item2 < 0:
                quotnt = "Skipped"
                rmdr = "Skipped"
            else:
                quotnt = item1 / item2
                rmdr = item1 % item2
            newlist.append(total)
            newlist.append(diff)
            newlist.append(prod)
            newlist.append(quotnt)
            newlist.append(rmdr)
            print(" ")
            print(f"Items: {item1}, {item2}")
            print(f"Addition: {total}")
            print(f"Subtraction: {diff}")
            print(f"Multiplication: {prod:.2f}")
            if quotnt == "Skipped":
                print("Division:", quotnt)
                print(f"Remainder: {rmdr:.2f}")
            elif rmdr == "Skipped":
                print(f"Division: {quotnt:.2f}")
                print(f"Remainder:", rmdr)
            elif quotnt == "Skipped" and rmdr == "Skipped":
                print("Division:", quotnt)
                print(f"Remainder:", rmdr)
            else:
                print(f"Division: {quotnt:.2f}")
                print(f"Remainder: {rmdr:.2f}")
            print(" ")

while choice < 2:
    print("Input List 1 item count:", end=" ")
    icount = int(input())

    print("Input List 1 items:", end=" ")
    list1 = [int(input()) for x in range (icount)]

    print("Input List 2 item count:", end=" ")
    iicount = int(input())

    print("Input items:", end=" ")
    list2 = [int(input()) for x in range(iicount)]

    complexnumbers(list1, list2)

    print("Continue adding numbers?")
    print("1 - Yes")
    print("2 - No")
    choice = (int(input()))

print("Thank you for using!")