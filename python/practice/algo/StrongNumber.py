# Factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Check Strong Number
def is_strong(number):
    temp = number
    sum_fact = 0
    while temp > 0:
        digit = temp % 10
        sum_fact += factorial(digit)
        temp //= 10
    return sum_fact == number

# Strong numbers in range
def get_strong_numbers(start, end):
    counter = 0
    for num in range(start, end+1):
        if is_strong(num):
            print(num, end=", ")
            counter += 1
    return counter

print("Strong Numbers in a given range")
x = int(input("Enter start value: "))
y = int(input("Enter last value: "))
count = get_strong_numbers(x, y)
print(f"\nCount = {count}")
