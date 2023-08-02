def isprime(num):
    if num == 1 or num == 0 :
        return False
    for i in range (2,num):
        if num % i == 0 :
            return "This is not prime number"
    return "This is a prime number"
n=int(input("Enter a number : "))
print(isprime(n))