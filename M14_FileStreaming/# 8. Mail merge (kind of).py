# 6. Enough Deadlock, let's get a mail merge going
# Difficulty: Hard
def letterer(item):                                                         # Defines a function "letterer" which takes strings for the letter
    print("")
    print(f"To {item},")
    print(f"Hello. I hope this letter finds you well.")
    print(f"You have been invited to a grand event.")
    print(f"yapyapyapyap.")
    print("")

def mailmerger():                                                           # Defines a function "mailmerger" which prints the outputs into a .txt
    with open("letter.txt", "a") as file:
        file.write(f"To {item},\n")
        file.write(f"Hello. I hope this letter finds you well.\n")
        file.write(f"You have been invited to a grand event.\n")
        file.write(f"yapyapyapyap.\n")


print("Input item count:", end=" ")
icount = int(input())

print("Input items:", end=" ")
list = [input() for x in range(icount)]

print(" ")
print("Recipients:", *list, sep=", ")

with open("recipients.txt", "w") as file:
    for item in list:
        file.write(f"{item}\n")

for item in list:
    letterer(item)
    mailmerger()