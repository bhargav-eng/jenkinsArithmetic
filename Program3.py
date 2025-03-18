import os

# Get the upper limit for the prime number calculation from the environment variable
upper_limit = int(os.environ.get('UPPER_LIMIT', 10))  # Default to 10 if not provided

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Calculate the sum of prime numbers up to the upper limit
prime_sum = 0
for num in range(2, upper_limit + 1):
    if is_prime(num):
        prime_sum += num

# Display the result
print(f"The sum of prime numbers up to {upper_limit} is: {prime_sum}")

