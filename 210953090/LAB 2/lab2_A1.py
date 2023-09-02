# Dictionary to store cached results
fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    # Cache the result before returning it
    fibonacci_cache[n] = result
    return result

# Calculate and print Fibonacci numbers using memoization
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")
