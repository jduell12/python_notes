"""
Model online store in Python
"Design an online store where customers can purchase products from vendors. Vendors need to be able to create the products that customers can then purchase"

- From sentence find the nouns 
    - Users
        - Customers
        - Vendors
        - Admin
    - Products
    - Purchases
- From the sentence the adjectives will be the attributes
     - Users
        * name
        * is the user an admin?
        - Customers
            * name
            * collection of purchases
        - Vendors
            * name 
            * collection of products
        - Admin
            * name
            * flag that the user is admin
    - Products
        * name
        * price
        * vendor
    - Purchases
        * product
        * customer
        * price
        * date and time info about when purchase was completed
- Relationships between the objects
    - Customers have purchases (one to many)
    - Vendors have products (one to many)
    - Purchases have products (one to many)
"""

from datetime import datetime


class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


class Customer(User):  # inherits from User
    def __init__(self, name):
        super().__init__(name)
        self.purchases = []

    def purchase_product(self, product):
        purchase = Purchase(product, self)
        self.purchases.append(purchase)


class Vendor(User):  # inherits from User
    def __init__(self, name):
        super().__init__(name)
        self.products = []

    def create_product(self, product_name, product_price):
        product = Product(self, product_name, product_price)
        self.products.append(product)


class Admin(User):
    def __init__(self, name):  # inherits from User
        super().__init__(name, is_admin=True)


class Product:
    def __init__(self, name, price, vendor):
        self.name = name
        self.price = price
        self.vendor = vendor


class Purchase:
    def __init__(self, product, customer):
        self.product = product
        self.customer = customer
        self.purchase_price = product.price
        self.purchase_date = datetime.now()

####################################################################


class Student:
    def __init__(self, first_name, last_name):  # initializes object
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):  # prints out easily readable object
        return 'Student: %s %s' % (self.first_name, self.last_name)

    def __repr__(self):  # returns 'offical' string rep of object
        return 'Student(first_name = %s, last_name = %s)' % (self.first_name, self.last_name)


student = Student('Jessica', 'Duell')
print(student.first_name, student.last_name)
print(student)
