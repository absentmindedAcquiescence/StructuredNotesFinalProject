# 6. Two number operations
# Difficulty: Intermediate
def simplenumbers(a, b):
    print(f"Addition: {a + b:.2f}")
    print(f"Subtraction: {a - b:.2f}")
    print(f"Multiplication: {a * b:.2f}")
    if a > 0 and b > 0:
        print(f"Division: {a / b:.2f}")
        print(f"Remainder: {a % b:.2f}")
    else:
        print("Division: Skipped")
        print("Remainder: Skipped")

print("Operate on numbers?")
print("1 - Yes")
print("2 - No")
choice = (int(input()))

while choice < 2:
    print("Input two numbers:", end=" ")
    a = int(input())
    b = int(input())

    print(f"Input: {a, b}")
    simplenumbers(a, b)

    print("Continue operating on numbers?")
    print("1 - Yes")
    print("2 - No")
    choice = (int(input()))

print("Thank you for using!")