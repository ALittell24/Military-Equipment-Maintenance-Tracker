#Maintenance tracker to maintain updated info regarding equipment status

import json

equipment_list = []


def save_data():
    with open("equipment_data.json", "w") as file:
        json.dump(equipment_list, file, indent=4)


def load_data():
    global equipment_list
    try:
        with open("equipment_data.json", "r") as file:
            equipment_list = json.load(file)
    except FileNotFoundError:
        equipment_list = []


def add_equipment():
    name = input("Enter equipment name: ")
    serial_number = input("Enter serial number: ")
    last_maintenance = input("Enter last maintenance date: ")
    next_maintenance = input("Enter next maintenance date: ")
    status = input("Enter status (Ready / Needs Maintenance / Down): ")

    equipment = {
        "name": name,
        "serial_number": serial_number,
        "last_maintenance": last_maintenance,
        "next_maintenance": next_maintenance,
        "status": status
    }

    equipment_list.append(equipment)
    save_data()
    print("Equipment added successfully!")


def view_equipment():
    if len(equipment_list) == 0:
        print("No equipment records found.")
        return

    for index, equipment in enumerate(equipment_list, start=1):
        print(f"\nEquipment #{index}")
        print(f"Name: {equipment['name']}")
        print(f"Serial Number: {equipment['serial_number']}")
        print(f"Last Maintenance: {equipment['last_maintenance']}")
        print(f"Next Maintenance: {equipment['next_maintenance']}")
        print(f"Status: {equipment['status']}")


def search_equipment():
    search_serial = input("Enter serial number to search: ")

    for equipment in equipment_list:
        if equipment["serial_number"] == search_serial:
            print("\nEquipment Found:")
            print(f"Name: {equipment['name']}")
            print(f"Serial Number: {equipment['serial_number']}")
            print(f"Last Maintenance: {equipment['last_maintenance']}")
            print(f"Next Maintenance: {equipment['next_maintenance']}")
            print(f"Status: {equipment['status']}")
            return

    print("No equipment found with that serial number.")


def update_status():
    search_serial = input("Enter serial number to update: ")

    for equipment in equipment_list:
        if equipment["serial_number"] == search_serial:
            new_status = input("Enter new status: ")
            equipment["status"] = new_status
            save_data()
            print("Status updated successfully!")
            return

    print("No equipment found with that serial number.")


def main_menu():
    while True:
        print("\n--- Military Equipment Maintenance Tracker ---")
        print("1. Add Equipment")
        print("2. View All Equipment")
        print("3. Search Equipment")
        print("4. Update Equipment Status")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_equipment()
        elif choice == "2":
            view_equipment()
        elif choice == "3":
            search_equipment()
        elif choice == "4":
            update_status()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


load_data()
main_menu()
