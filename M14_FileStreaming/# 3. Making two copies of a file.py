# 3. Make two copies of your file, one for the Archmother and the other for the Hidden King
# Difficulty: Easy
print("Input text:", end=" ")
text = input()

with open("M14_FileStreaming/hero.txt", "w") as f:
    f.write(text)  

print("")

with open("M14_FileStreaming/AMallied.txt", "w") as f:                                                # The first copy goes to the Archmother.
    f.write(text)  
with open("M14_FileStreaming/AMallied.txt", "a") as f:
    f.write(f"\n> The information contained within your bytes...")                                    # This is appended so you know who it's for.
    f.write(f"\n> Summon the Archmother, and they shall remain for eternity.")

with open("M14_FileStreaming/HKallied.txt", "w") as f:                                                # The second copy goes to the Hidden King.
    f.write(text)  
with open("M14_FileStreaming/HKallied.txt", "a") as f:
    f.write(f"\n> The information contained within your bytes...")                  
    f.write(f"\n> Summon the Hidden King, and you can gain so much more.")

with open("M14_FileStreaming/AMallied.txt") as f:                                                     # You can check by having Python print the readouts.
    print(f.read())  

print("")

with open("M14_FileStreaming/HKallied.txt") as f:
    print(f.read())  