# Check Armstrong Number
def is_armstrong(number):
    digits = str(number)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == number

# Armstrong numbers in range
def get_armstrong_numbers(start, end):
    counter = 0
    for num in range(start, end+1):
        if is_armstrong(num):
            print(num, end=", ")
            counter += 1
    return counter

print("Armstrong Numbers in a given range")
x = int(input("Enter start value: "))
y = int(input("Enter last value: "))
count = get_armstrong_numbers(x, y)
print(f"\nCount = {count}")
