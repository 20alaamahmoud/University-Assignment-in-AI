def palindrome(str):
    word=str[::-1]
    if str == word:
        return "PALINDROME"
    return "NOT Palindrome"
st=input("Enter a string : ")
print(palindrome(st))