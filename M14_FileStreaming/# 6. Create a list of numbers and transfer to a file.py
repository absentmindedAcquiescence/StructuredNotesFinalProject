# 6. Transfer numbers to a file
print("Input number to multiply:", end=" ")
n = int(input())

for i in range(1, n + 1):
    grid = []
    for j in range(1, n + 1):
        grid.append(i * j)
        with open("multiplicationwow.txt", "a") as file:
                file.write(f"{i * j} \n")

with open("multiplicationwow.txt") as file:
    print(file.read())