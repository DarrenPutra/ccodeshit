def compoundinterest(principle, rate, year):
    if year == 0:
        return principle
    else:
        principle = principle*(1+rate)
        return compoundinterest(principle , rate, year-1)
    
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

