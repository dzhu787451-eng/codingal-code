vowel=['a', 'e', 'i', 'o', 'u']
word=input("Please enter a word: ")
for i in word:
    if i in vowel:
        print("Your Vowel is", i)
    else:
        continue

