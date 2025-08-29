import mysql.connector

class ProductIdError(Exception):
    pass

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password@1",
        database="ansi"
    )

def is_product_list_empty():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM product")
    count = cursor.fetchone()[0]
    conn.close()
    return count == 0

def product_exists(pid):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE pid = %s", (pid,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def insert_product(product):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO product (pid, name, category, quantity, price) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, product)
    conn.commit()
    print("Product inserted.")
    conn.close()

def display_products():
    if is_product_list_empty():
        print("No products.")
        return
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def updateProduct(pid):
    if is_product_list_empty():
        print("No products ")
        return
    if not product_exists(pid):
        print("Product ID not found.")
        choice = input("Do you want to insert it as a new product?").strip().lower()
        if choice == "yes":
            name = input("Enter name: ")
            category = input("Enter category: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            insert_product((pid, name, category, quantity, price))
        else:
            print("Update cancelled.")
        return
    conn = connect_db()
    cursor = conn.cursor()
    name = input("Enter new name: ")
    category = input("Enter new category: ")
    quantity = int(input("Enter new quantity: "))
    price = float(input("Enter new price: "))
    query = "UPDATE product SET name=%s, category=%s, quantity=%s, price=%s WHERE pid=%s"
    cursor.execute(query, (name, category, quantity, price, pid))
    conn.commit()
    print("Product updated.")
    conn.close()

def delete_prouduct(pid):
    if is_product_list_empty():
        print("No products ")
        return
    if not product_exists(pid):
        raise ProductIdError("Product ID does not exist.")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE pid=%s", (pid,))
    conn.commit()
    print("Product deleted.")
    conn.close()

def search_proudct(pid):
    if is_product_list_empty():
        print("No products ")
        return
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE pid=%s", (pid,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("Product not found.")
    conn.close()

def menu():
    while True:
        print("\n1. Insert Product")
        print("2. Display Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            pid = int(input("Enter Product ID: "))
            name = input("Enter Name: ")
            category = input("Enter Category: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            insert_product((pid, name, category, quantity, price))
        elif choice == '2':
            display_products()
        elif choice == '3':
            pid = int(input("Enter Product ID to update: "))
            updateProduct(pid)
        elif choice == '4':
            pid = int(input("Enter Product ID to delete: "))
            try:
                delete_prouduct(pid)
            except ProductIdError as e:
                print("Error:", e)
        elif choice == '5':
            pid = int(input("Enter Product ID to search: "))
            search_proudct(pid)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    menu()
