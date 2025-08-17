def check_positive_negative(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print("Check Positive / Negative / Zero")
num = int(input("Enter a number: "))
print(f"{num} is {check_positive_negative(num)}")
