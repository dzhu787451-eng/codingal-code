# 1) Ask the user to enter a word or sentence and store it in `text`.
# 2) Reverse the string stored in `text` and store the reversed result in `revText`.
#    (Reversing means the last character becomes first, and the first becomes last.)
# 3) Replace `text` with the reversed string (set `text` equal to `revText`).
# 4) Print a message saying you are showing the reversed string.
# 5) Print the reversed string stored in `text`.
text=input("enter a word or a sentence")
revText=text[::-1]
print("I will show the reversed text")
#text=revText
print(revText)
print("I will show the uppercase and lowercase for the text")
print(text.upper())
print(text.lower())
str1="good"
print(str1+text)
print(str1[0:1])
print(str1[0:3])
print(str1[1:4])
print(str1[1:3])