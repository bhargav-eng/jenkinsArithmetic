# Function to generate Fibonacci sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Get the first 10 Fibonacci numbers
n = 10
fib_sequence = fibonacci(n)

# Print the Fibonacci sequence
print(f"The first {n} Fibonacci numbers are: {fib_sequence}")

