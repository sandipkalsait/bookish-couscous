def calculate_rate(age, area):
    area = area.lower()
    if age < 18:
        return 5 if area == "rural" else 4
    elif age < 60:
        return 7 if area == "rural" else 6
    else:
        return 10 if area == "rural" else 8

def calculate_investment(age, amount, area):
    rate = calculate_rate(age, area)
    interest = (amount * rate) / 100
    total = amount + interest
    return rate, interest, total

print("Investment Calculator")
age = int(input("Enter age: "))
amount = float(input("Enter amount to deposit: "))
area = input("Enter area (rural/urban): ")

rate, interest, total = calculate_investment(age, amount, area)
print(f"Rate of Interest = {rate}%")
print(f"Interest Earned = {interest}")
print(f"Total Amount = {total}")
