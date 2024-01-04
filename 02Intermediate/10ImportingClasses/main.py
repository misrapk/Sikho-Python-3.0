"""from <moduleName> import <className>"""
from products import Book, Clothing, Electronics, Product
# import products
# from products import *    """NOt Recommended"""
# import products as prod

#TODO: Write
def saveProducts(products, filename):
    with open(filename, 'w') as files:
        for product in products:
            files.write(f"{product.name}, {product.price}, {product.description}\n")


#TODO: Read
def loadProducts(filename):
    products =[]
    try:
        with open(filename, "r") as files:
            for line in files:
                name, price, description = line.strip().split(",")
                products.append(Product(name, price, description))
        print("Products loaded in list!")
    
    except FileNotFoundError:
        print(f"{filename} dosenot exist")
        products = []
    
    return products



laptop = Electronics("Asus Vivobook", 800000, "16 GB SSD Laptop", "ASUS")
book1 = Book("One Indian Girl", 300, "a story about An indian girl", "Chetan Bhagat", "Romantic")
tshirt = Clothing("Tshirt", 800, "Puma Tshirt", "M", "Black")

# laptop.productDetails()
# book1.productDetails()
# tshirt.productDetails()

products = [laptop, book1, tshirt]

saveProducts(products, "productsInfo.txt")

loadedProduct = loadProducts("productsInfoi.txt")

for product in loadedProduct:
    product.productDetails()