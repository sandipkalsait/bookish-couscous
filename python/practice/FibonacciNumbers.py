def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Generate series
def fibonacci_series(limit):
    return [fibonacci(i) for i in range(limit)]

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Generate series
def fibonacci_series(limit):
    return [fibonacci(i) for i in range(limit)]


limit = int(input("Enter how many Fibonacci terms you want: "))
series = fibonacci_series(limit)
print("Fibonacci Series:", series)
