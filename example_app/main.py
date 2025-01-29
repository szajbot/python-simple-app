import requests

API_BASE_URL = "http://localhost:8000"

def get_cars():
    response = requests.get(f"{API_BASE_URL}/cars")
    if response.status_code == 200:
        print("Cars: \n", response.json())
    else:
        print("Failed to retrieve cars.")

def get_car_drivers():
    response = requests.get(f"{API_BASE_URL}/drivers")
    if response.status_code == 200:
        print("Drivers: \n", response.json())
    else:
        print("Failed to retrieve drivers.")

def get_car():
    car_id= input("Enter car ID to retrieve: ")
    response = requests.get(f"{API_BASE_URL}/car/{car_id}")
    if response.status_code == 200:
        print("Car Details:\n", response.json())
    else:
        print("Failed to retrieve car details.")

def get_car_driver():
    driver_id = input("Enter driver ID to retrieve: ")
    response = requests.get(f"{API_BASE_URL}/driver/{driver_id}")
    if response.status_code == 200:
        print("Driver Details: \n", response.json())
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
    response = requests.post(f"{API_BASE_URL}/car", json=car)
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
    response = requests.put(f"{API_BASE_URL}/car/{car_id}", json=car)
    if response.status_code == 200:
        print("Car updated successfully.")
    else:
        print("Failed to update car.")

def delete_car():
    car_id = input("Enter car ID to delete: ")
    response = requests.delete(f"{API_BASE_URL}/car/{car_id}")
    if response.status_code == 204:
        print("Car deleted successfully.")
    else:
        print("Failed to delete car.")

def create_driver():
    name = input("Enter new name: ")
    driver = {
        "name": name,
    }
    response = requests.post(f"{API_BASE_URL}/driver", json=driver)
    if response.status_code == 200:
        print("Car created successfully.")
    else:
        print("Failed to create car.")

def update_driver():
    driver_id = input("Enter driver ID to update name: ")
    name = input("Enter new name: ")
    driver = {
        "name": name,
    }
    response = requests.patch(f"{API_BASE_URL}/driver/{driver_id}", json=driver)
    if response.status_code == 200:
        print("Driver name updated successfully.")
    else:
        print("Failed to update driver name.")

def delete_driver():
    driver_id = input("Enter driver ID to delete: ")
    response = requests.delete(f"{API_BASE_URL}/driver/{driver_id}")
    if response.status_code == 204:
        print("Driver deleted successfully.")
    else:
        print("Failed to delete car.")

def main_menu():
    while True:
        print("\nAPI Client")

        print("1. Get All Cars")
        print("2. Get All Drivers")

        print("3. Get Car")
        print("4. Get Car Driver")

        print("5. Create a Car")
        print("6. Update a Car")
        print("7. Delete a Car")

        print("8. Create a Car")
        print("9. Update a Car")
        print("10. Delete a Car")

        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            get_cars()
        elif choice == '2':
            get_car_drivers()

        elif choice == '3':
            get_car()
        elif choice == '4':
            get_car_driver()

        elif choice == '5':
            create_car()
        elif choice == '6':
            update_car()
        elif choice == '7':
            delete_car()

        elif choice == '8':
            create_driver()
        elif choice == '9':
            update_driver()
        elif choice == '10':
            delete_driver()

        elif choice == '11':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()