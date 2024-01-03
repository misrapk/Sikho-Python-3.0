class Product:   #parent Class
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.descirption = description
        
    def productDetails(self):
        print("\nDetails of the Product: ")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Description: {self.descirption}")
        
#child Class - inherited from Product class
class Book(Product):
    def __init__(self, name, price, description, author, genre):
         super().__init__(name, price, description)
         self.author = author
         self.genre = genre
    
    #MEthod Override
    def productDetails(self):
        super().productDetails()
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
         
class Clothing(Product):
    def __init__(self, name, price, description, size, color):
         super().__init__(name, price, description)
         self.size = size
         self.color = color
         
    def productDetails(self):
        super().productDetails()
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")
         
class Electronics(Product):
    def __init__(self, name, price, description, brand):
         super().__init__(name, price, description)
         self.brand = brand
         
    def productDetails(self):
        super().productDetails()
        print(f"Brand: {self.brand}")

class MobilePhone(Electronics):
    def __init__(self, name, price, description, brand, network, camera):
        super().__init__(name, price, description, brand)
        self.network = network
        self.camera = camera
    
    def productDetails(self):
        super().productDetails()
        print(f"Network: {self.network}")
        print(f"Camera: {self.camera}")
    
         
         
book1 = Book("Wings of Fire", 300, "A Biography of Dr. APJ ABDUL KALAM", "DR. Kalam", "Biography")
electronic1 = Electronics("Smart Watch", 1500, "A Smart Watch", "Boat")
cloth1 = Clothing("Tshirt", 500, "Round Neck Tshirt", "S", "Black")
redmi = MobilePhone("Note 12", 12500, "A new Redmi Smart phone", "REDMI", "5G", "200MP")

book1.productDetails()
electronic1.productDetails()
cloth1.productDetails()
redmi.productDetails()
        
# cloth = Product("Shirt", 250, "Checked Shirt")
# cloth.productDetails()