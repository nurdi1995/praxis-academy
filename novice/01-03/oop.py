class Dog:
    #class Attribut
    species ='mamalia'
    #inisialisasi atribut 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    #inisialisasi objek dog
    jake = Dog("Jake", 7)
    doug = Dog("Doug", 4)
    william = Dog("william",5)
    #Dterminan
    def get_biggest_number(*args):
        return max(args)
    
    print("Umur dari Dog adalah ".format(get_biggest_number(jake.age,doug.age, william.age)))
        