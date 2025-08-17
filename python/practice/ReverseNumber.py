def reverse_number(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    return rev

print("Reversing the Number")


x=int(input("Enter the number\t:\t"))

print(f"\n number {x} reversed is {reverse_number(x)}");