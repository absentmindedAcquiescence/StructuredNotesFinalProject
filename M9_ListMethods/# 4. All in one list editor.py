# 4. All in one list editor
def lister():
    print("Choose next operation:")
    print("1 - Add to list")
    print("2 - Edit list")
    print("3 - Remove item from list")
    print("4 - Exit")
    choice = (int(input()))

    match choice:
        case 1:
            print("Input item count:", end=" ")
            icount = int(input())

            print("Input items:", end=" ")
            for x in range(icount):
                list.append(input()) 

            print("List:", list)

            print("Continue operation?")
            print("1 - Yes")
            print("2 - No")
            choice2 = int(input())

            if choice2 == 2:
                print("Thank you for using!")
            else:
                lister()

        case 2:
            print("Input count target:", end=" ")
            ctarget = input()
            ctargetindex = list.index(ctarget)

            print("Target index:", ctargetindex)
            print("Input value to be inserted:", end=" ")
            new = list.insert(ctargetindex, input())
            list.pop()

            print("Updated list:", list)

            print("Continue operation?")
            print("1 - Yes")
            print("2 - No")
            choice2 = int(input())
            
            if choice2 == 2:
                print("Thank you for using!")
            else:
                lister()

        case 3:
            print("Input count target:", end=" ")
            ctarget = input()
            list.remove(ctarget)

            print("Updated list:", list)

            print("Continue operation?")
            print("1 - Yes")
            print("2 - No")
            choice2 = int(input())
            
            if choice2 == 2:
                print("Thank you for using!")
            else:
                lister()

        case 4:
            print("Thank you for using!")


print("Input item count:", end=" ")
icount = int(input())

print("Input items:", end=" ")
list = [input() for x in range(icount)]

print("List:", list)

lister()