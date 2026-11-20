# 4. Export your .py file into a .txt
# Difficulty: Intermediate
with open("M14_FileStreaming/# 4. Export your file into another file.py") as file:      # Opens this file itself
    script = [file.read()]                                                              # Reads line by line into a list

with open("M14_FileStreaming/textcopy.txt", "w") as file:                               # Creates a text copy
    for item in script:                                                                 
        file.write(f"{item}")                                                           # Writes every item in the script list line by line

with open("textcopy.txt") as file:
    print(file.read())                                                                  # Check the readout here