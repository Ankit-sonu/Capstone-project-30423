from product import Product
from productdao import ProductDAO
from productservice import ProductService

def menu():
    dao = ProductDAO()
    service = ProductService(dao)
    while True:
        print("\n--- Product Management Menu ---")
        print("1. Add Product")
        print("2. Display All Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                productid = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                category = input("Enter Product Category: ")
                quantity = int(input("Enter Product Quantity: "))
                price = float(input("Enter Product Price: "))
                product = Product(productid, name, category, quantity, price)
                service.add_product(product)
                print("Product added successfully!")
            except Exception as e:
                print("Error:", e)
        elif choice == '2':
            try:
                products = service.get_all_products()
                for product in products:
                    print(product)
            except Exception as e:
                print("Error:", e)
        elif choice == '3':
            try:
                productid = int(input("Enter Product ID to update: "))
                existing = service.get_product(productid)
                if not existing:
                    print("Product not found!")
                    continue
                name = input(f"Enter new name [{existing.name}]: ") or existing.name
                category = input(f"Enter new category [{existing.category}]: ") or existing.category
                quantity = input(f"Enter new quantity [{existing.quantity}]: ") or existing.quantity
                price = input(f"Enter new price [{existing.price}]: ") or existing.price
                updated_product = Product(productid, name, category, int(quantity), float(price))
                service.update_product(productid, updated_product)
                print("Product updated successfully!")
            except Exception as e:
                print("Error:", e)
        elif choice == '4':
            try:
                productid = int(input("Enter Product ID to delete: "))
                if service.delete_product(productid):
                    print("Product deleted successfully!")
                else:
                    print("Product not found!")
            except Exception as e:
                print("Error:", e)
        elif choice == '5':
            try:
                productid = int(input("Enter Product ID to search: "))
                product = service.get_product(productid)
                if product:
                    print(product)
                else:
                    print("Product not found.")
            except Exception as e:
                print("Error:", e)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()

