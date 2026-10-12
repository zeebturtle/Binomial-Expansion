from fractions import Fraction

def factorial(number):
   if not isinstance(number, int):
       return "Please enter an integer as the factorial"

   if number < 0:
       return "Factorial is not defined for negative numbers"

   result = 1

   while number > 1:
       result *= number
       number -= 1

   return result

print("""Welcome to the binomial expansion calculator.

The calculator is designed to give approximations to irrational numbers to a degree of accuracy that you choose.

Enter a fractional power between -1 and 1, enter the amount of terms you'd like involved in your approximated expansion
(The more terms, the more accurate your approximation will be), and enter a non-zero positive base.

Powers that are recurring numbers such as 1/3 will always be approximated to 15 decimals places by default.

There are always at least two terms, 1 and nx.
""")

base = float(Fraction(input("What is the base:")))
n = float(Fraction(input("What is the power:")))
accuracy = int(input("How many terms would you like (minimum:2):"))

def binomialexpansion(base, n):

    if n >= 1 or n <= -1:
        return "The power must be a fraction between -1 and 1"

    if base <= 0:
        return "The base must be a positive value"

    if accuracy < 2:
        return "The minimum number of terms is 2"

    count = 0

    while base > 2:

        base /= 4

        count += 1

    multiplier_power = n * count

    multiplier = 4 ** multiplier_power

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

    series *= multiplier

    return str(series)

print(binomialexpansion(base, n))

#Goal: to make accuracy measurable.

#The current expansion loses convergence speed as base tends to 0

#Iterating the factorial causes an overflow error for large numbers of terms. Find a way to create the next term based on the previous one rather than iterating so much.

#Maybe I should consider using the binomialexpansion function for irrational powers such as 1/3? It would give me an
#approximation rather than a stored decimal value. At the same time, it could make the expansion less accurate,