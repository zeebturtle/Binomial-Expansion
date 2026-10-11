def factorial( number ):
    if not isinstance(number, int):
        print("Please enter an integer as the factorial")

    while number >1:
        number * number - 1

factorial(5)