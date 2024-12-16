#DOCSTRING
def factorial(factor):
    """This function is for calculating the factorial of a numver that is provided, it will automatically compute the factorial of the provided number."""
    fact = 1
    for x in range(factor, 0, -1):
        fact *= x
        print(fact)
    return fact

factorial(5)

help(factorial)