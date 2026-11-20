# 8. Editing a dictionary
# Difficulty: Hard
dict = {

    }

def quickfix():

    print("What operation would you like to perform?")
    print("1. Add names")
    print("2. Update names")
    print("3. Delete names")
    print("4. Exit")
    choice = int(input())

    match choice:
        case 1:
            print("Input person count:", end=" ")
            icount = int(input())

            for _ in range(icount):
                print("Input name:", end=" ")
                name = input()

                print("Input associated value:", end=" ")
                contact = int(input())

                dict[name] = contact

            print(f"Dictionary: {dict}")

            print("Continue operation?")
            print("1 - Yes")
            print("2 - No")
            choice2 = int(input())
            
            if choice2 == 2:
                print("Thank you for using!")
            else:
                quickfix()
        
        case 2:
            print("Input name you'd like to change:", end=" ")
            name = input()

            dict.pop(name)

            print("Input new name:", end=" ")
            name = input()

            print("Input new associated value:", end=" ")
            contact = int(input())
            
            dict[name] = contact

            print(f"Dictionary: {dict}")

            print("Continue operation?")
            print("1 - Yes")
            print("2 - No")
            choice2 = int(input())
            
            if choice2 == 2:
                print("Thank you for using!")
            else:
                quickfix()

        case 3:
            print("Input name you'd like to delete:", end=" ")
            name = input()

            dict.pop(name)
            print("Name removed.")
            print(f"New dictionary: {dict}")

            print("Continue operation?")
            print("1 - Yes")
            print("2 - No")
            choice2 = int(input())
            
            if choice2 == 2:
                print("Thank you for using!")
            else:
                quickfix()

        case 4:
            print("Thank you for using!")

        case _:
            print("Invalid input. Please try again:")
            print("1. Add names")
            print("2. Update names")
            print("3. Delete names")
            print("4. Exit")
            choice = int(input())


quickfix()