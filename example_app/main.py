import requests

API_BASE_URL = "http://localhost:8000"

def get_cars():
    response = requests.get(f"{API_BASE_URL}/cars/")
    if response.status_code == 200:
        print("Cars: \n", response.json())
    else:
        print("Failed to retrieve cars.")

def get_car():
    car_id= input("Enter car ID to retrieve: ")
    response = requests.get(f"{API_BASE_URL}/cars/{car_id}")
    if response.status_code == 200:
        print("Car Details:\n", response.json())
    else:
        print("Failed to retrieve car details.")

def get_car_driver():
    car_id = input("Enter car ID: ")
    response = requests.get(f"{API_BASE_URL}/cars/{car_id}/driver")
    if response.status_code == 200:
        print("Car Driver: \n", response.json())
    else:
        print("Failed to retrieve car driver.")

def create_car():
    brand= input("Enter car brand: ")
    model = input("Enter car model: ")
    driver_id = input("Enter driver ID: ")
    car = {
        "brand": brand,
        "model": model,
        "driver_id": int(driver_id)}
    response = requests.post(f"{API_BASE_URL}/cars/", json=car)
    if response.status_code == 200:
        print("Car created successfully.")
    else:
        print("Failed to create car.")

def update_car():
    car_id = input("Enter car ID to update: ")
    brand= input("Enter new brand: ")
    model = input("Enter new model: ")
    driver_id = input("Enter new driver ID: ")
    car = {
    "brand": brand,
    "model": model,
    "driver_id": int(driver_id)
    }
    response = requests.put(f"{API_BASE_URL}/cars/{car_id}", json=car)
    if response.status_code == 200:
        print("Car updated successfully.")
    else:
        print("Failed to update car.")

def update_driver_name():
    driver_id = input("Enter driver ID to update name: ")
    name = input("Enter new name: ")
    response = requests.patch(f"{API_BASE_URL}/drivers/{driver_id}/name", json={"name": name})
    if response.status_code == 200:
        print("Driver name updated successfully.")
    else:
        print("Failed to update driver name.")

def delete_car():
    car_id = input("Enter car ID to delete: ")
    response = requests.delete(f"{API_BASE_URL}/cars/{car_id}")
    if response.status_code == 204:
        print("Car deleted successfully.")
    else:
        print("Failed to delete car.")

def main_menu():
    while True:
        print("\nAPI Client")
        print("1. Get All Cars")
        print("2. Get Car Driver")
        print("3. Create a Car")
        print("4. Update a Car")
        print("5. Delete a Car")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            get_cars()
        elif choice == '2':
            get_car_driver()
        elif choice == '3':
            create_car()
        elif choice == '4':
            update_car()
        elif choice == '5':
            delete_car()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "_main_":
    main_menu()