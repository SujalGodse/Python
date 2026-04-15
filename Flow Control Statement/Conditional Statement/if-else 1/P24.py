#WAP to check whether a given character is a vowel or consonant. if vowel , to print the next character of a given character or else print previous characters.

char = input("Enter a character: ").lower()
if char in 'aeiou':
    print("Next character:",chr(ord(char) + 1))
else:
    print("Previous character:",chr(ord(char) - 1))