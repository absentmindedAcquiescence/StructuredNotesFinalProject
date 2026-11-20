# 2. A function using string methods to print text cases
# Difficulty: Easy
def quirkinator(word): 
    print(f"UPPERCASE: {word.upper()}") 
    print("lowercase:", word.lower())
    print("Capitalized Case:", word.title())
    CC = word.title()
    if word.endswith("."):
        print(f"Sentence case: {word.capitalize()}")
    else:
        print(f"Sentence case: {word.capitalize()}.")
    print(f"tOGGLE cASE: {CC.swapcase()}")

print("Input word, phrase, or sentence:", end=" ")
word = input()
quirkinator(word)