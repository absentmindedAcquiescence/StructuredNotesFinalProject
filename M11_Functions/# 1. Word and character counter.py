# 1. Word and character counter
# Difficulty: Easy
def checker(word):                                          # Defines a function that checks a string (word)
    print(f'Input: "{word}"')                               # It prints what it will operate on
    if " " in word:                                         # if statement checks for words through spaces
        print(f"Character count: {len(word)}")
        print(f"Word count: {len(word.split(" "))}")        # Should it find any, it will split the string into a list using .split()
    else: 
        print(f"Character count: {len(word)}")
        print(f"Word count: Just 1 :)")                     # Should it not, it will say you only have one word



print("Input word, phrase, or sentence:", end=" ")          # Try it yourself!
word = str(input())
checker(word)