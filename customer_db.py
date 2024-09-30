import mysql.connector

# MySQL connection setup
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # Change this to your MySQL username
        password="yourpassword",   # Change this to your MySQL password
        database="customer_db"     # The database you created in MySQL
    )

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        address VARCHAR(255) NOT NULL,
                        email VARCHAR(100) NOT NULL,
                        phone VARCHAR(20) NOT NULL)''')
    conn.commit()
    conn.close()

def add_customer(name, address, email, phone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, address, email, phone) VALUES (%s, %s, %s, %s)",
                   (name, address, email, phone))
    conn.commit()
    conn.close()
    print("Customer added successfully!")

def view_customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_customer(customer_id, name, address, email, phone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE customers SET name = %s, address = %s, email = %s, phone = %s WHERE id = %s""",
                   (name, address, email, phone, customer_id))
    conn.commit()
    conn.close()
    print("Customer updated successfully!")

def delete_customer(customer_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
    conn.commit()
    conn.close()
    print("Customer deleted successfully!")

def main_menu():
    while True:
        print("\nCustomer Database Management System")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            add_customer(name, address, email, phone)

        elif choice == '2':
            customers = view_customers()
            for customer in customers:
                print(customer)

        elif choice == '3':
            customer_id = int(input("Enter customer ID to update: "))
            name = input("Enter new name: ")
            address = input("Enter new address: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            update_customer(customer_id, name, address, email, phone)

        elif choice == '4':
            customer_id = int(input("Enter customer ID to delete: "))
            delete_customer(customer_id)

        elif choice == '5':
            print("Exiting system.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
