# 1. Creating your file
# Difficulty: Easy
print("Input text:", end=" ")                                     # Takes your input
text = input()

with open("M14_FileStreaming/helloworld.txt", "w") as file:       # The most standard way to operate on files is with the with function
    file.write(text)                                              # This line writes our input to a .txt called "helloworld" inside M14_FileStreaming

with open("M14_FileStreaming/helloworld.txt") as file:            # This opens the file, simple as
    print(file.read())                                            # Then prints it