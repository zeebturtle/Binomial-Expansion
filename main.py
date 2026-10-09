from fractions import Fraction

dedasdadad
    if number < 0:
        return "Factorial is not defined for negative numbers"

    result = 1

    while number > 1:
        result *= number
        number -= 1

    return result

print("""Welcome to the binomial expansion calculator. 

The calculator is designed to give approximations to irrational numbers to a degree of accuracy that you choose.

Enter a fractional power between zero and one, enter the amount of terms you'd like involved in your approximated expansion 
(The more terms, the more accurate your approximation will be), and enter a non-zero base between -1 and 1.

Powers that are recurring numbers such as 1/3 will always be approximated to 15 decimals places by default.

There are always at least two terms, 1 and nx.
""")

base = float(input("What is the base:"))
n = float(Fraction(input("What is the power:")))
accuracy = int(input("How many terms would you like (minimum:2):"))

def binomialexpansion(base, n):

    if n >= 1 and n <= -1:
        return "The power must be a fraction between 0 and 1"

    if base < 0:
        return "The base must be a positve, non-zero integer"

    x = base - 1

    series = 1 + (n * x)

    iterated_number = -1
    iterated_factorial = 2
    iterated_power = 2

    denominator = factorial(iterated_factorial)
    numerator = (n * (n + iterated_number))

    term = numerator / denominator

    for i in range(2, accuracy):

        series += (term * (x ** iterated_power))

        iterated_number -= 1
        iterated_factorial += 1
        iterated_power += 1

        numerator *= (n + iterated_number)
        denominator = factorial(iterated_factorial)

        term = numerator / denominator

    return str(series)

print(binomialexpansion(base, n))
