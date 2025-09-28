import datetime

def accept_products():
    products = {}

    while True:
        pid = input("Enter productId (numeric): ").strip()
        if not pid.isnumeric():
            print("Invalid productId!")
            continue
        pid = int(pid)

        if pid in products:
            print("Product ID already exists!")
            continue

        name = input("Enter product name: ").strip()
        if not name.replace(" ", "").isalpha():
            print("Invalid name!")
            continue

        price = input("Enter price (>5000): ").strip()
        if not price.replace(".", "", 1).isnumeric():
            print("Invalid price!")
            continue
        price = float(price)
        if price <= 5000:
            print("Price must be greater than 5000!")
            continue

        qty = input("Enter quantity: ").strip()
        if not qty.isnumeric():
            print("Invalid quantity!")
            continue
        qty = int(qty)

        products[pid] = {"name": name, "price": price, "quantity": qty}
        print(f"Product {pid} added successfully.")

        more = input("Add another product? YES/NO: ").strip().lower()
        if more != "yes":
            break

    return products


def write_file(filename, items):
    f = open(filename, "w")
    f.write("productId name price quantity\n")
    for pid, d in items.items():
        f.write(str(pid) + " " + d['name'] + " " + str(d['price']) + " " + str(d['quantity']) + "\n")
    f.close()


def write_files(products):
    today = datetime.date.today()
    date_str = str(today.day)+ "_" + str(today.month)+ "_" + str(today.year)

    main_file = "data_" + date_str + ".txt"
    price1_file = "price1.txt"
    price2_file = "price2.txt"

    # Filter products with price >= 5000 and write to price1_file
    filtered_products1 = {}
    for pid, d in products.items():
        if d["price"] >= 5000:
            filtered_products1[pid] = d
    write_file(price1_file, filtered_products1)

    # Filter products with price >= 10000 and write to price2_file
    filtered_products2 = {}
    for pid, d in products.items():
        if d["price"] >= 10000:
            filtered_products2[pid] = d
    write_file(price2_file, filtered_products2)

    return [main_file, price1_file, price2_file]


def display_files(files):
    for file in files:
        print("\n--- " + file + " ---")
        f = open(file, "r")
        print(f.read())
        f.close()


def main():
    products = accept_products()
    files = write_files(products)
    display_files(files)


main()
