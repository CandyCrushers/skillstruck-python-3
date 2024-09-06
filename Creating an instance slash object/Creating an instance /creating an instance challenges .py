# Fruit Festival


'''class Fruit: 

    def __init__(self, shape, kind, size):
        self.shape = shape 
        self.kind = kind 
        self.size = size 


f1 = Fruit("Round", "Apple", "Large")
f2 = Fruit("Round", "Grape", "Small")
f3 = Fruit("Round", "Blueberry", "Small")
f4 = Fruit("Round", "Watermelon", "XL")

print(f1.kind)
print(f2.kind)
print(f3.kind)
print(f4.kind)''' 


# ----------------------------------------------------------------------

'''class Pet: 

    def __init__(self, size, breed, gender):
        self.size = size 
        self.breed = breed 
        self.gender = gender 


pet = Pet("Small", "Whipit", "Female")
pet1 = Pet("Big", "Dalmation", "Male")
pet2 = Pet("Small", "Bulldog", "Female")


print(pet.size)
print(pet1.breed)
print(pet2.gender)'''

# ----------------------------------------------------------------------


class Vacation: 

    def __init__(self, location, activity, food):
        self.location = location 
        self.activity = activity 
        self.food = food 


vac = Vacation("Italy", "Sight Seeing", "Pizza, Pasta")
vac1 = Vacation("France", "Countryside", "French Food")
vac2 = Vacation("China", "Great Wall", "Chinese Food")



print("I like going to " + vac.location + " It is unique as its not like " + vac.activity + " however, it doesnt have " + vac.food)
print("I like going to " + vac1.location + " It is unique as its not like " + vac1.activity + " however, it doesnt have " + vac1.food)
print("I like going to " + vac2.location + " It is unique as its not like " + vac2.activity + " however, it doesnt have " + vac2.food)

