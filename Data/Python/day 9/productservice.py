
class ProductService:
    def __init__(self, dao):
        self.dao = dao

    def add_product(self, product):
        return self.dao.add_product(product)

    def get_product(self, productid):
        return self.dao.get_product(productid)

    def get_all_products(self):
        return self.dao.get_all_products()

    def delete_product(self, productid):
        return self.dao.delete_product(productid)

    def update_product(self, productid, product):
        return self.dao.update_product(productid, product)
