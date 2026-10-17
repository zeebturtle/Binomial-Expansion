from fractions import Fraction

#created factorial function for use in the expansion

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

print("""
Welcome to the binomial expansion calculator. Please read below for information on how to use the calculator.

The calculator is designed to give approximations to irrational numbers to a degree of accuracy that you choose.

Enter a fractional, non-zero power in the form x/y where x is the numerator and y is the denominator between -1 and 1, enter the amount of terms you'd like involved in your approximated expansion
(The more terms, the more accurate your approximation will be), and enter a non-zero positive base.

There are always at least two terms, 1 and nx.
The maximum number of terms that you can select is 160.

Python will naturally round any inputted value to about 15-17 significant decimal digits. This may mean that the accuracy of your approximation may be different to what you'd expect if you are inputting very small or very large values.

Convergence speed may vary depending on your value of base. What this means essentially is that for different values of base, the approximation may be more/less accurate for the same number of terms.

""")

error_explanation = None

while error_explanation != "Y" or error_explanation != "N":
    error_explanation = input("Would you like to see an explanation of the error system (Y/N):")
    if error_explanation == "Y":
        print("""

The estimated error is the value of the next 10 terms of the expansion.
                
The percentage error indicates how far your approximation differs from Python's stored value, expressed as a percentage.
Negative percentage error: Your approximation is smaller than Python's stored value.
Positive percentage error: Your approximation is larger than Python's stored value.
Zero percentage error: Your approximation is the same as Python's stored value, or the calculated difference between the approximation and python's stored value is too small to represent.
The magnitude of the percentage indicates the size of the difference relative to Python's stored value
                
Error values may be in scientific notation form, xe-y. The e is a constant, 10. e-y means 10^-y, and you multiply this value by x, so xe-y means x multiplied by 10^-y. You may also plug in values using scientific notation.
""")
    if error_explanation == "N":
        break
    if error_explanation != "Y" or error_explanation != "N":
        print("Please enter Y or N")

# Verification

base = None
while base == None:
    try:
        base = float(Fraction(input("What is the base: ")))
        if base <= 0:
            print("The base must be a positive non-zero value. Please try again.")
            base = None  # Reset so it repeats the loop
    except (OverflowError):
        print("Your base is too large")
    except (ValueError, ZeroDivisionError):
        print("Please enter an integer, decimal or fraction as the base.")

n = None
while n == None:
    try:
        n = float(Fraction(input("What is the power: ")))
        if n >= 1 or n <= -1:
            print("The power must be a fraction between -1 and 1. Please try again.")
            n = None  # Reset so it repeats the loop
        if n == 0:
            print("Either you have entered a power with a value of zero, or the value you have entered is too small.")
            n = None
    except (ValueError, ZeroDivisionError):
        print("Please enter a decimal or fraction as the power.")

accuracy = None
while accuracy == None:
    try:
        accuracy = int(input("How many terms would you like (minimum: 2, maximum: 160): "))
        if accuracy < 2:
            print("The minimum number of terms is 2. Please try again.")
            accuracy = None
        elif accuracy > 160:
            print("The maximum number of terms is 160. Please try again.")
            accuracy = None
    except (ValueError, ZeroDivisionError):
        print("Please enter an integer as the number of terms you would like.")

def binomialexpansion(base, n):

    # Scaling loop part 1. Satisfies 0 < base < 2 before expanding so that the series can converge

    base_scaled = base
    count = 0
    multiplier = 1

    # Scaling loop part 2. Scales down base_scaled further to get it between 0.5 and 2 so that convergence speed can be faster

    while base_scaled >= 2:
        base_scaled /= 4
        count += 1
        multiplier = (4 ** count) ** n

    while base_scaled < 0.5:
        base_scaled *= 4
        count += 1
        multiplier = 1/(4 ** count) ** n

    #Binomial expansion loop. Based on the generalized binomial theorem

    x = base_scaled - 1

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

    #Expanding the series further to find error

    series_for_error = series

    for i in range(accuracy, accuracy + 10):
        series_for_error += (term * (x ** iterated_power))
        iterated_number -= 1
        iterated_factorial += 1
        iterated_power += 1
        numerator *= (n + iterated_number)
        denominator = factorial(iterated_factorial)
        term = numerator / denominator

    series *= multiplier

    #calculating estimated error

    series_for_error *= multiplier
    estimated_error = abs(series_for_error - series)

    #calculating percentage error

    python_value = base ** n
    percentage_error = series - python_value / python_value * 100

    if series == 1 and n != 0:
        print(f"The power you have entered may be too small for python to calculate the difference between terms, resulting in an approximation of 1 for {base} ^ {n}.")
    else:
        print(f"The approximated value for {base} ^ {n} is:",str(series))

    if estimated_error != 0:
        print(f"The estimated error for your value is {estimated_error}")
    else:
        print("The calculated difference between the two sums is too small to represent at python's standard floating-point precision. Therefore the estimated error cannot be calculated.")

    if percentage_error != 0:
        print(f"The percentage error when compared with python's stored value for {base} ^ {n} is {percentage_error}")
    elif (series - python_value) == 0:
        print(f"Either the approximated value is the same as pythons stored value or the calculated difference between the approximated value and python's stored value for {base} ^ {n} is smaller than python's floating-point precision limit and therefore percentage error cannot be represented.")

binomialexpansion(base, n)

#The current expansion loses convergence speed as base tends to 0 or 2, and it gains convergence speed as it tends to 1.