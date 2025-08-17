def largest_of_three(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print("Find the Largest of Three Numbers")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
print(f"Largest number is {largest_of_three(x, y, z)}")
