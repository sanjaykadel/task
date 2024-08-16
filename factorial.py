import math

def factorial(n):  #(n) -> parameter or number that to be calculated 
    if n == 1 or n == 0:
        print(f"factorial({n}) = 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"factorial({n}) = {n} * factorial({n-1}) = {result}")
        return result

# Function to check if a number is a perfect square
def is_perfect_square(x):
    sqrt = math.isqrt(x)
    return sqrt * sqrt == x

def main():
    # Enter Number
    n = int(input("Enter a positive integer: "))

    if n < 0:
        print("Please enter a positive integer.")
        return

    # Calculate the factorial
    fact = factorial(n)

    print(f"\nFactorial of {n} is: {fact}")

    # Check if the factorial is a perfect square
    if is_perfect_square(fact):
        print(f"{fact} is a perfect square.")
    else:
        print(f"{fact} is not a perfect square.")

if __name__ == "__main__":
    main()
