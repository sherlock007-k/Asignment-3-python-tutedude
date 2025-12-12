def factorial(n):
    n_fact = 1
    for i in range(1,n+1):
        n_fact = n_fact*i
    print(f"factorial of {n} is : {n_fact}")
    return n_fact    

a = int(input("enter a number : "))

factorial(a)
