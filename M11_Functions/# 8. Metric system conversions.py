# 8. Metric system conversions
# Difficulty: Hard
def millimetrifier(a, b = 10):
    print(f"Input: {a}")
    print(f"To millimeters: {a * b} mm")
    print(f"To centimeters: {a / b:.2f} cm")
    print(" ")

def centimetrifier(a, b = 100):
    print(f"Input: {a}")
    print(f"To centimeters: {a * b} cm")
    print(f"To meters: {a / b:.2f} m")
    print(" ")

def metrifier(a, b = 1000):
    print(f"Input: {a}")
    print(f"To meters: {a * b} m")
    print(f"To kilometers: {a / b:.2f} km")
    print(" ")

def units():
    print("Choose operation: ")
    print("1 - Millimeters to centimeters")
    print("2 - Centimeters to meters")
    print("3 - Meters to kilometers")
    print("4 - Exit")
    choice = int(input())

    match choice:
        case 1:
            print("Input item:", end=" ")
            a = int(input())

            millimetrifier(a)

            print("Continue operation?")
            print("1 - Yes")
            print("2 - No")
            choice2 = int(input())

            if choice2 == 2:
                print("Thank you for using!")
            else:
                units()

        case 2:
            print("Input item:", end=" ")
            a = int(input())

            centimetrifier(a)

            print("Continue operation?")
            print("1 - Yes")
            print("2 - No")
            choice2 = int(input())
            
            if choice2 == 2:
                print("Thank you for using!")
            else:
                units()

        case 3:
            print("Input item:", end=" ")
            a = int(input())

            metrifier(a)

            print("Continue operation?")
            print("1 - Yes")
            print("2 - No")
            choice2 = int(input())
            
            if choice2 == 2:
                print("Thank you for using!")
            else:
                units()

        case 4:
            print("Thank you for using!")

units()