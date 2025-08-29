def __init__(self, productid, name, category, quantity, price):
    self.productid = productid
    self.name = name
    self.category = category
    self.quantity = quantity
    self.price = price


def __repr__(self):
    return f"Product(ID={self.productid}, Name='{self.name}', Category='{self.category}', Quantity={self.quantity}, Price={self.price})"
