# 3. Even more string methods for text cases
# Difficulty: Intermediate
print("Input word, phrase, or sentence:", end=" ")
word = input()
PC = word.title()
altlist = PC.split(" ")
list = word.split(" ")

def caseinator(word):
    sc = "_".join(list)
    kc = "-".join(list)
    dc = ".".join(list)
    TC = "-".join(altlist)
    PC = "".join(altlist)
    print(f"snake_case: {sc.lower()}")
    print(f"kebab-case: {kc.lower()}")
    print(f"dot.case: {dc.lower()}")
    print(f"SCREAMING_SNAKE_CASE: {sc.upper()}")
    print(f"PascalCase: {PC}")
    print(f"Train-Case: {TC}")

print("Input:", *list)
caseinator(word)