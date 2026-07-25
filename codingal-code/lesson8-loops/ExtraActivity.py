string=input("Enter a word or sentence: ")
string2=""
length=0
for i in string:
    length=length+1
    string2=i+string2
print("The length of the word/sentence is:", length)
print("The word/sentence reversed is:", string2)