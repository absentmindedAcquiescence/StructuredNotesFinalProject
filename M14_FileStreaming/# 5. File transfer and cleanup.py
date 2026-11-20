# 5. ESCAPE THE HOTEL (file transfer + cleanup)
# Difficulty: Intermediate
text = []                                       # Remember the poor guest from earlier? Let's save them. Hold onto this list.

with open("guest.txt") as file:                 # Let's look at this file copy...
    for line in file:
        text.append(line)                       # Save it to our list...
    text.pop()                                  # And get rid of the signature on the bottom!

with open("guest.txt", "w") as file:
    pass                                        # Clear the file too!

with open("saved.txt", "w") as file:            # Now that we've saved the poor thing, let's put him in a new .txt file!
    for tx in text:
        file.write(tx)                          

with open("saved.txt") as file:                 # Check the contents to ensure he's truly freed from The Doorman.
    print(file.read())