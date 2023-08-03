def ispangram(s):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    for char in ALPHABET:
        if char not in s.lower():
            return "NOT Pangram"
    return "Pangram"
words=input("Enter some words : ")
print(ispangram(words))