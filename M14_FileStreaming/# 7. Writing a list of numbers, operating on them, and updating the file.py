# 7. Operating on numbers from a file and updating it
# Difficulty: Hard
def numfiler():
    print("Input item count:", end=" ")
    icount = int(input())
    
    print("Input items:", end=" ")
    list = [int(input()) for x in range(icount)]                    # In case you want to input the list yourself
    
    with open("lotsanumbers.txt", "w") as file:
            for item in list:
                file.write(f"{item} \n")

    return list

def randnumfiler():
    import random

    text = [random.randint(1, 10) for _ in range(1, 10)]            # In case you don't want to input a list yourself

    with open("lotsanumbers.txt", "w") as file:
        for tx in text:
            file.write(f"{tx} \n")

    return text

newlist = []

print("Input number to add:", end=" ")
number = int(input())

print("Create list?")
print("1 - yes")
print("2 - no")
choice = int(input())

if choice < 2:
    list = numfiler()
    print(f"List: {list}")

    for item in list:
        newlist.append(item + number)

    print(f"Operated list: {newlist}")
    

else:
    list = randnumfiler()
    print(f"Randomized list: {list}")

    for item in list:
        newlist.append(item + number)

    print(f"Operated list: {newlist}")


with open("lotsanumbers.txt", "w") as file:
    for newitem in newlist:
        file.write(f"{newitem}\n")