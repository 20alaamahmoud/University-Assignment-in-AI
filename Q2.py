def strin(s):
    up=0
    lo=0
    for i in s:
        if i.isupper():
            up+=1
        elif i.islower():
            lo+=1
    print("The number of UPPER case characters is = ", up)
    print("The number of lower case characters is = ", lo)
st=input("Enter any string : ")
print(strin(st))