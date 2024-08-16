import math

# Optimized recursive function with memoization to calculate factorial
def calculate_factorial(n, memo={}):
    # Base case
    if n in (0, 1):
        print(f"factorial({n}) = 1")
        return 1

    # Check garne ki factorial already compute bhako cha ki chaina (memoization)
    if n in memo:
        return memo[n]

    # Recursive step with intermediate step display
    result = n * calculate_factorial(n - 1, memo)
    print(f"factorial({n}) = {n} * factorial({n-1}) = {result}")

    # Result future ma feri use garna store garne (memoization)
    memo[n] = result
    return result

# Function check garne ki number perfect square ho ki hoina
def is_perfect_square(x):
    sqrt = math.isqrt(x)
    return sqrt * sqrt == x

def main():
    while True:
        # User lai input dina prompt garne
        user_input = input("Enter a positive integer: ")

        # Input validation: check garne ki input numeric cha ki chaina
        if not user_input.isdigit():
            print("Invalid input! Please enter a positive integer.")
            continue

        n = int(user_input)

        # Check garne ki input positive integer ho ki hoina
        if n < 0:
            print("Kripaya sakaratmak integer dinuhos (0 ya tyasko bhandaa mathi).")
            continue

        # Factorial calculate garne
        fact = calculate_factorial(n)

        print(f"\nFactorial of {n} is: {fact}")

        # Check garne ki factorial perfect square ho ki hoina
        if is_perfect_square(fact):
            print(f"{fact} perfect square ho.")
        else:
            print(f"{fact} perfect square hoina.")
        
        # Valid input receive bhaye pachi loop break garne
        break

if __name__ == "__main__":
    main()
