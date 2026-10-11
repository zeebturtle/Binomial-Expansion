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
(The more terms, the more accurate your approximation will be), and enter a non-zero base between between 0 and 2.

Powers that are recurring numbers such as 1/3 will always be approximated to 15 decimals places by default.

There are always at least two terms, 1 and nx.
""")

base = float(Fraction(input("What is the base:")))
n = float(Fraction(input("What is the power:")))
accuracy = int(input("How many terms would you like (minimum:2):"))

def binomialexpansion(base, n):

    if n >= 1 or n <= -1:
               return "The power must be a fraction between -1 and 1"

    if base <= 0 or base > 2:
               return "The base must be a positive, non-zero integer between 0 and 2"

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


#The reason for why the base can only be as high as 2 is because the modulus of x must be less than 1. Currently, my code
#solves for x by doing x = base -1, therefore, a base such as 15 would yield the modulus of x having to be less than 1/14,
#which is mathematically impossible to solve using my current code. I'm not sure that even I completely understand the problem myself, so
#any help or advice on making the range of values for the base larger will be appreciated, as a range of 0 to 2 is pretty useless.



