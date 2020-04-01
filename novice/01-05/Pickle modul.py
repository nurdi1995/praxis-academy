import pickle
class Animal:
    def __init__(self, number_of_paws, color):
        self.number_of_paws = number_of_paws
        self.color = color

class Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)

mary = Sheep("White")

#1
print(str.format("My sheep mary is {0} and has {1} paws", mary.color, mary.number_of_paws))
my_pickled_mary = pickle.dumps(mary)

print ("Would you like to see her pickled? here she is!")
print(my_pickled_mary)

#2
binary_file = open('my_pickled_mary.bin', Mode='wb')
my_pickled_mary = pickle.dump(mary, binary_file)
binary_file.close()

#3
dolly = pickle.load(my_pickled_mary)
dolly.color = "black"

print (str.format("Dolly is {0}", dolly.color))
print (str.format("Marry is {0}", mary.color))