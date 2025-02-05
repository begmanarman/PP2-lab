def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get user input and convert it into a list of integers
num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Use filter function to extract prime numbers
prime_numbers = list(filter(is_prime, num_list))

# Print the result
print("Prime numbers:", prime_numbers)

