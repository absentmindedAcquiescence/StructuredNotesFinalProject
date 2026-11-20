# 5. Unique word counter using a dictionary
# Difficulty: Intermediate
print("Input word, phrase, or sentence:", end=" ")
word = input().strip()

if " " in word: 
    uniqword = {}
    punc = ',.:;!?"'
    for i in punc:
        word = word.replace(i, " ")

    cleanword = [clean.lower() for clean in word.split(" ") if len(clean) > 0 and not clean.isspace()]
    sword = sorted(cleanword)

    print(f"Character count: {len(word)}")
    print(f"Word count: {len(cleanword)}")
    print(f"Unique words and count:")
    for wor in sword:
        indivcount = cleanword.count(wor)
        if indivcount <= 1:
            uniqword[wor] = indivcount
    for k, v, in uniqword.items():
        print(f'"{k}" count: {v}')

else: 
    print(f"Character count: {len(word)}")
    print(f"Word count: Just 1 :)")