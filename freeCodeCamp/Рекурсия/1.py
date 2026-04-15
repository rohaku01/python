def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

print(factorial(5))



def recur_factorial(n):
    if n == 1:
        return n 
    
    temp = recur_factorial(n-1)
    temp *= n
    return temp

print(recur_factorial(5))