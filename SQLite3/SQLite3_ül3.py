import sqlite3
import csv

# establish a connection to the database and create a cursor
conn = sqlite3.connect('C:/sqlite/epood_kjoarand.db')
cursor = conn.cursor()

# define the functions for the menu
def add_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    car_make = input("Enter car make: ")
    car_model = input("Enter car model: ")
    car_year = int(input("Enter car year: "))
    car_price = float(input("Enter car price: "))
    cursor.execute("INSERT INTO kjoarand (first_name, last_name, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, email, car_make, car_model, car_year, car_price))
    conn.commit()
    print("Data added successfully!")
    
def show_cars_older_than_2000():
    cursor.execute("SELECT * FROM kjoarand WHERE car_year < 2000 ORDER BY car_year ASC")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No cars found!")
    else:
        for row in rows:
            print(row)

def show_avg_year_and_most_expensive_price():
    cursor.execute("SELECT AVG(car_year), MAX(car_price) FROM kjoarand")
    row = cursor.fetchone()
    print(f"Average year of cars: {row[0]}")
    print(f"Most expensive car price: {row[1]}")

def show_5_most_recent_car_makes():
    cursor.execute("SELECT DISTINCT car_make, car_model FROM kjoarand ORDER BY car_year DESC LIMIT 5")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No cars found!")
    else:
        for row in rows:
            print(f"{row[0]} - {row[1]}")

def show_5_most_expensive_car_brands_sorted_by_last_name():
    cursor.execute("SELECT kjoarand.last_name, kjoarand.car_make, SUM(kjoarand.car_price) as total_price FROM kjoarand GROUP BY kjoarand.car_make ORDER BY total_price DESC, kjoarand.last_name ASC LIMIT 5")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No cars found!")
    else:
        for row in rows:
            print(f"{row[0]} - {row[1]}")

def delete_data_by_id():
    id = int(input("Enter ID to delete: "))
    cursor.execute("DELETE FROM kjoarand WHERE id=?", (id,))
    conn.commit()
    print("Data deleted successfully!")

def delete_data_by_year_and_brand():
    year = int(input("Enter year: "))
    brand = input("Enter brand: ")
    cursor.execute("DELETE FROM kjoarand WHERE car_year < ? AND car_make = ?", (year, brand))
    conn.commit()
    print("Data deleted successfully!")

def export_to_csv():
    cursor.execute("SELECT * FROM kjoarand")


while True:
    choice = input("Choose an option:\n"
        "1. Add data\n"
        "2. Show cars older than 2000\n"
        "3. Show average year and most expensive price\n"
        "4. Show 5 most recent car makes\n"
        "5. Show 5 most expensive car brands sorted by last name\n"
        "6. Delete data by ID\n"
        "7. Delete data by year and brand\n"
        "8. Export to CSV\n"
        "0. Exit\n"
        "Enter your choice: ")
    
    if choice == "" or choice == "0":
        break
    
    elif choice == "1":
        add_data()
        
    elif choice == "2":
        show_cars_older_than_2000()
        
    elif choice == "3":
        show_avg_year_and_most_expensive_price()
        
    elif choice == "4":
        show_5_most_recent_car_makes()
        
    elif choice == "5":
        show_5_most_expensive_car_brands_sorted_by_last_name()
        
    elif choice == "6":
        delete_data_by_id()
        
    elif choice == "7":
        delete_data_by_year_and_brand()
        
    elif choice == "8":
        export_to_csv()
        
    else:
        print("Invalid choice. Please enter a number between 0 and 8.")