def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the value to get factorial: "))
res=factorial(n)
print(f"Factorial of {n} is {res}")