# 2. Make a copy of your file, to be checked into The Baroness
# Difficulty: Easy
print("Input text:", end=" ")
text = input()                                                              # Takes user input, you know the deal

with open("M14_FileStreaming/person.txt", "w") as f:
    f.write(text)  

with open("M14_FileStreaming/guest.txt", "w") as f:                         # This writes person.txt's contents into another file called guest.txt...
    f.write(text)  
with open("M14_FileStreaming/guest.txt", "a") as f:
    f.write(f"\n> Welcome. I hope you enjoy your stay.")                    # The Doorman will then append his "signature" onto the file to let you know this is the copy.

with open("M14_FileStreaming/guest.txt") as f:                              # You can check the file again.
    print(f.read())  