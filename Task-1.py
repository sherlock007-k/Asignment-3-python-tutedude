def factorial(n):
    b = n
    if n == 0:
        return 1
    else:
        n = n*factorial(n-1)   
    return n    

a = int(input("enter a number : "))

print(f"factorial of {a} is {factorial(a)}")


