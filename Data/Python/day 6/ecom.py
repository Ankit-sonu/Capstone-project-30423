class Product:
    def __init__(self, name, price): self.name = name; self.price = price

class Book(Product):
    def __init__(self, name, price, author): super().__init__(name, price); self.author = author

class Clothing(Product):
    def __init__(self, name, price, size): super().__init__(name, price); self.size = size

class Electronics(Product):
    def __init__(self, name, price, warranty): super().__init__(name, price); self.warranty = warranty

b = Book("Python", 10, "Alice")
c = Clothing("Shirt", 20, "M")
e = Electronics("Phone", 300, 2)
print(b.name, b.author)
print(c.name, c.size)
print(e.name, e.warranty)
