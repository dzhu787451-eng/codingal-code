string=input("Enter a word or sentence: ")
vowels=0
vowelslist=['a','e','i','o','u']
consonant=0
for i in string:
    if i in vowelslist:
        vowels+=1
    else:
        consonant+=1
print("The number of vowels is:", vowels)
print("The number of consonants is:", consonant)
