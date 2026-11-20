# 7. Updating a dictionary
# Difficulty: Intermediate
print("Input person count:", end=" ")
icount = int(input())
dict = {}

for _ in range(icount):
    print("Input name:", end=" ")
    name = input()

    print("Input associated value:", end=" ")
    value = int(input())

    dict[name] = value

print(f"Dictionary: {dict}")

print("Change name?")
print("1 - Yes")
print("2 - No")
choice = int(input())

while choice < 2:
    print("Input name you'd like to change:", end=" ")
    name = input()

    dict.pop(name)

    print("Input new name:", end=" ")
    name = input()

    print("Input new value:", end=" ")
    value = int(input())
                
    dict[name] = value

    print(f"Dictionary: {dict}")

    print("Change more names?")
    print("1 - Yes")
    print("2 - No")
    choice = int(input())


print("Thank you for using!")