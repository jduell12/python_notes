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

# User class


class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin
