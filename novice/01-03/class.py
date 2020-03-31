class Product:
    __vendor_message = "ini adalah rahasia"
    name=""
    price=""
    size = ""
    unit = ""

    def __init__(self, name):
        print ("ini adalah constuctor")
        self.name = name
        self.unit ="ml"
        self.size = 250

    def get_vendor_message(self):
        print (self.__vendor_message)
    
    def set_price(self,price):
        self.price = price

p = Product("Ultora Milek")
p.set_price(5500)

print("% dengan ukuran %s%s harganya Rp. %d"(p.name, p.size, p.unit, p.price))
#Print p.__vendor_message
# 
p.get_vendor_message()

p1 = Product("indomilk")
p1.set_price(50000)

print("% dengan ukuran %s%s harganya Rp. %d"(p.name, p.size, p.unit, p.price))

print (p == p)
print (p1 == p1)
print (p == p1)

