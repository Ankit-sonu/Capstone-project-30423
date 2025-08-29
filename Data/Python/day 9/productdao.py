
import mysql.connector
from product import Product

class ProductDAO:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@1",
            database="training"
        )
        self.cursor = self.conn.cursor()

    def add_product(self, product):
        sql = "INSERT INTO product (productid, name, category, quantity, price) VALUES (%s, %s, %s, %s, %s)"
        values = (product.productid, product.name, product.category, product.quantity, product.price)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def get_product(self, productid):
        sql = "SELECT * FROM product WHERE productid = %s"
        values = (productid,)
        self.cursor.execute(sql, values)
        row = self.cursor.fetchone()
        if row:
            return Product(*row)
        return None

    def get_all_products(self):
        sql = "SELECT * FROM product"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return [Product(*row) for row in rows]

    def delete_product(self, productid):
        sql = "DELETE FROM product WHERE productid = %s"
        values = (productid,)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def update_product(self, productid, product):
        sql = "UPDATE product SET name=%s, category=%s, quantity=%s, price=%s WHERE productid=%s"
        values = (product.name, product.category, product.quantity, product.price, productid)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.rowcount > 0
