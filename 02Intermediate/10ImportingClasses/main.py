"""from <moduleName> import <className>"""

# from products import Product, Book
# import products
# from products import *    """NOt Recommended"""

import products as prod

# p1 = Product("Jeans",250, "Blue Jeans Pant")
# p1.productDetails()
book1 = prod.Book("One Indian Girl", 300, "a story about An indian girl", "Chetan Bhagat", "Romantic")
book1.productDetails()


tshirt = prod.Clothing("Tshirt", 800, "Puma Tshirt", "M", "Black")
tshirt.productDetails()

