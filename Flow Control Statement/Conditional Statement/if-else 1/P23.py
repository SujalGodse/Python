#WAP to check whether the input character is a vowel or not. If it is vowel print ‘VOWEL’ along with that character, if it is not just print ‘CONSONANT’.

char = input("Enter a character : ").lower()
if char in ("a","e","i","o","u"):
    print("VOWEL :",char)
else:
    print("CONSONANT :",char)