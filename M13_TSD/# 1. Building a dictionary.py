# 1. Building a dictionary
# Difficulty: Easy
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