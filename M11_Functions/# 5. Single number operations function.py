# 5. Single number operations for a list
# Difficulty: Easy
def simplernumbers(a):
    print(f"Added to itself: {a + a}")
    print(f"Multiplied by itself: {a * a}")
    print(f"Itself as the exponent: {a ** a}")

print("Operate on numbers?")
print("1 - Yes")
print("2 - No")
choice = int(input())

while choice < 2:
    print("Input item count:", end=" ")
    icount = int(input())

    print("Input items:", end=" ")
    list = [int(input()) for x in range(icount)]

    for item in list:
        simplernumbers(item)

    print("Continue operating on numbers?")
    print("1 - Yes")
    print("2 - No")
    choice = (int(input()))

print("Thank you for using!")
