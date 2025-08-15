#  Dictionary CRUD
#  Use Functions Only
#     1 To add an element
#     2 To update an element
#     3 To delete an element
#     4 To validate values

# Sample records
sample_records = {
    101: {"name": "Mobile", "type": "Mobile", "status": "Active"},
    102: {"name": "Laptop", "type": "Laptop", "status": "Inactive"},
    103: {"name": "Router", "type": "Network Module", "status": "Active"}
}

DEVICE_TYPES = ["Mobile", "Laptop", "Desktop", "Router", "Bridge", "Network Module"]
DEVICE_STATUS = ["Active", "Inactive", "Maintenance"]

# ------------------ Functions ------------------ #
def print_menu():
    print("""
    #------------- Device CRUD Menu -------------#
    1. Add Device
    2. Update Device
    3. Delete Device
    4. Show Device Records
    0. Exit
    """)

def validate(key, value):
    if key == "device_id":
        if not value.isdigit():
            print("Warning: Device ID must be numeric!")
            return False
    elif key == "name":
        if not value.replace(" ", "").isalpha():
            print("Warning: Device name must contain only letters!")
            return False
    elif key == "type":
        if value not in DEVICE_TYPES:
            print(f"Warning: Device type must be one of {DEVICE_TYPES}")
            return False
    elif key == "status":
        if value not in DEVICE_STATUS:
            print(f"Warning: Status must be one of {DEVICE_STATUS}")
            return False
    return True

def is_exist(records, device_id):
    return device_id in records

def add_device(records):
    while True:
        value = input("Enter Device ID (unique, numeric): ").strip()
        if not validate("device_id", value):
            continue
        device_id = int(value)
        if is_exist(records, device_id):
            print("Device ID already exists!")
            continue

        name = input("Enter Device Name: ").strip()
        if not validate("name", name):
            continue

        print("Device Types:", ", ".join(DEVICE_TYPES))
        device_type = input("Enter Device Type: ").strip()
        if not validate("type", device_type):
            continue

        print("Device Status Options:", ", ".join(DEVICE_STATUS))
        status = input("Enter Device Status: ").strip()
        if not validate("status", status):
            continue

        records[device_id] = {"name": name, "type": device_type, "status": status}
        print(f"Device {device_id} added successfully.")

        more = input("Add another device? YES/NO: ").strip().lower()
        if more != "yes":
            break
    return records

def update_device(records):
    while True:
        value = input("Enter Device ID to update: ").strip()
        if not validate("device_id", value):
            continue
        device_id = int(value)

        if not is_exist(records, device_id):
            print("Device ID not found!")
            more = input("Try another Device ID? YES/NO: ").strip().lower()
            if more != "yes":
                break
            continue

        print("Leave blank to keep current value.")
        name = input(f"Enter new Name ({records[device_id]['name']}): ").strip()
        if name:
            if validate("name", name):
                records[device_id]["name"] = name

        print("Device Types:", ", ".join(DEVICE_TYPES))
        device_type = input(f"Enter new Type ({records[device_id]['type']}): ").strip()
        if device_type:
            if validate("type", device_type):
                records[device_id]["type"] = device_type

        print("Device Status Options:", ", ".join(DEVICE_STATUS))
        status = input(f"Enter new Status ({records[device_id]['status']}): ").strip()
        if status:
            if validate("status", status):
                records[device_id]["status"] = status

        print(f"Device {device_id} updated successfully.")
        more = input("Update another device? YES/NO: ").strip().lower()
        if more != "yes":
            break
    return records

def delete_device(records):
    while True:
        value = input("Enter Device ID to delete: ").strip()
        if not validate("device_id", value):
            continue
        device_id = int(value)

        if is_exist(records, device_id):
            del records[device_id]
            print(f"Device {device_id} deleted.")
        else:
            print("Device ID not found!")

        more = input("Delete another device? YES/NO: ").strip().lower()
        if more != "yes":
            break
    return records

def show_devices(records):
    if not records:
        print("No device records found.")
    else:
        print("\nDevice Records:")
        for device_id, rec in records.items():
            print(f"{device_id}: {rec}")

            

# ------------------ Main ------------------ #
def main():
    records = sample_records.copy()
    functions = {
        1: add_device,
        2: update_device,
        3: delete_device,
        4: show_devices
    }
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if not choice.isdigit():
            print("Please enter a number.")
            continue
        choice = int(choice)
        if choice == 0:
            print("Exiting program...")
            break
        elif choice in functions:
            functions[choice](records)
        else:
            print("Invalid choice. Please try again.")

main()
